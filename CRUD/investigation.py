from schemas.investigations import CaseInvestigationsCreate, CaseInvestigationsUpdate
from models.investigationdatabase import InvestigationDB
from sqlalchemy import select
from sqlalchemy.orm import Session


# Nested schema names -> database column names
NESTED_FIELDS = {
    "cbc": [
        "hb", "tlc", "platelets", "hct",
        "neutrophils", "lymphocytes",
    ],
    "lft": [
        "total_bilirubin", "direct_bilirubin", "ast",
        "alt", "alp", "albumin", "total_protein",
    ],
    "kft": [
        "urea", "creatinine", "sodium",
        "potassium", "chloride",
    ],
    "pt_inr": ["pt", "inr"],
    "viralmarkers": ["hbsag", "anti_hcv", "hiv"],
    "extra": ["crp", "procalcitonin"],
}


def flatten_investigation(data: dict) -> dict:
    """Convert nested schema data into flat database columns."""
    flat_data = {}

    for key, value in data.items():
        if key not in NESTED_FIELDS:
            # Convert the API field name to the database field name.
            db_key = "investigation_type" if key == "investigationtype" else key
            flat_data[db_key] = value

    for group, fields in NESTED_FIELDS.items():
        nested_data = data.get(group)

        if nested_data is not None:
            for field in fields:
                flat_data[field] = nested_data.get(field)

    return flat_data


def investigation_to_nested(row: InvestigationDB) -> dict:
    """Convert a database record into the nested API structure."""
    result = {
        "investigation_id": row.investigation_id,
        "followup_id": row.followup_id,
        "investigationtype": row.investigation_type,
        "status": row.status,
        "ordered_at": row.ordered_at,
        "collected_at": row.collected_at,
        "reported_at": row.reported_at,
        "notes": row.notes,
    }

    for group, fields in NESTED_FIELDS.items():
        values = {field: getattr(row, field) for field in fields}

        # Return None if no results in this group have been recorded.
        result[group] = (
            values if any(value is not None for value in values.values())
            else None
        )

    result["blood_sugar"] = row.blood_sugar
    return result


def investigationcreate(db : Session, investigation : CaseInvestigationsCreate) -> InvestigationDB | None: 
    data = flatten_investigation(investigation.model_dump())
    new_investigation = InvestigationDB(**data)

    try: 
        db.add(new_investigation)
        db.commit()
        db.refresh(new_investigation)
        return investigation_to_nested(new_investigation)
    except Exception:
        db.rollback()
        raise

def investigationdelete(db:Session, investigation_id: int) -> bool | None:
    investigationtodelete = db.get(InvestigationDB, investigation_id)
    if investigationtodelete is None:
        return False

    try: 
        db.delete(investigationtodelete)
        db.commit()
        return True
    except Exception:
        db.rollback()
        raise

def investigationupdate(db: Session, investigation: CaseInvestigationsUpdate, investigation_id: int) -> InvestigationDB | None:
    investigationtoupdate = db.get(InvestigationDB, investigation_id)
    if investigationtoupdate is None:
        return None
    changes = flatten_investigation(
    investigation.model_dump(exclude_unset=True)
    )

    for field, value in changes.items():
        setattr(investigationtoupdate, field, value)

    try:
        db.commit()
        db.refresh(investigationtoupdate)
        return investigation_to_nested(investigationtoupdate)
    except Exception:
        db.rollback()
        raise

def readinvestigation(db: Session, investigation_id : int) -> InvestigationDB | None: 
    investigationtoread = db.get(InvestigationDB, investigation_id)
    return investigationtoread

def readinvestigationall(db: Session) -> list[dict]:
    statement = select(InvestigationDB)
    investigations = db.scalars(statement).all()

    return [
        investigation_to_nested(investigation)
        for investigation in investigations
    ]