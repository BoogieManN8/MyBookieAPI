from sqlalchemy.orm import Session
from app.models.log import Log
from app.schemas.log import LogCreate, LogUpdate

def get_log(db: Session, log_id: str):
    return db.query(Log).filter(Log.id == log_id).first()

def get_logs(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Log).offset(skip).limit(limit).all()

def create_log(db: Session, log: LogCreate):
    db_log = Log(**log.dict())
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log

def update_log(db: Session, log_id: str, log: LogUpdate):
    db_log = get_log(db, log_id)
    if db_log is None:
        return None
    update_data = log.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_log, key, value)
    db.commit()
    db.refresh(db_log)
    return db_log

def delete_log(db: Session, log_id: str):
    db_log = get_log(db, log_id)
    if db_log is None:
        return None
    db.delete(db_log)
    db.commit()
    return db_log
