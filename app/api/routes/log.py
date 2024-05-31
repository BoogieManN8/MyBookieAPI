from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.log import Log, LogCreate, LogUpdate
from app.crud import crud_log
from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=Log)
def create_log(log: LogCreate, db: Session = Depends(get_db)):
    return crud_log.create_log(db=db, log=log)

@router.get("/{log_id}", response_model=Log)
def read_log(log_id: str, db: Session = Depends(get_db)):
    db_log = crud_log.get_log(db, log_id=log_id)
    if db_log is None:
        raise HTTPException(status_code=404, detail="Log not found")
    return db_log

@router.get("/", response_model=List[Log])
def read_logs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    logs = crud_log.get_logs(db, skip=skip, limit=limit)
    return logs

@router.put("/{log_id}", response_model=Log)
def update_log(log_id: str, log: LogUpdate, db: Session = Depends(get_db)):
    db_log = crud_log.update_log(db, log_id=log_id, log=log)
    if db_log is None:
        raise HTTPException(status_code=404, detail="Log not found")
    return db_log

@router.delete("/{log_id}", response_model=Log)
def delete_log(log_id: str, db: Session = Depends(get_db)):
    db_log = crud_log.delete_log(db, log_id=log_id)
    if db_log is None:
        raise HTTPException(status_code=404, detail="Log not found")
    return db_log
