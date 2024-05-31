from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.match import Match, MatchCreate, MatchUpdate
from app.crud import crud_match
from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=Match)
def create_match(match: MatchCreate, db: Session = Depends(get_db)):
    return crud_match.create_match(db=db, match=match)

@router.get("/{match_id}", response_model=Match)
def read_match(match_id: str, db: Session = Depends(get_db)):
    db_match = crud_match.get_match(db, match_id=match_id)
    if db_match is None:
        raise HTTPException(status_code=404, detail="Match not found")
    return db_match

@router.get("/", response_model=List[Match])
def read_matches(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    matches = crud_match.get_matches(db, skip=skip, limit=limit)
    return matches

@router.get("/user/{user_id}", response_model=List[Match])
def read_user_matches(user_id: str, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    matches = crud_match.get_user_matches(db, user_id=user_id, skip=skip, limit=limit)
    return matches

@router.put("/{match_id}", response_model=Match)
def update_match(match_id: str, match: MatchUpdate, db: Session = Depends(get_db)):
    db_match = crud_match.update_match(db, match_id=match_id, match=match)
    if db_match is None:
        raise HTTPException(status_code=404, detail="Match not found")
    return db_match

@router.delete("/{match_id}", response_model=Match)
def delete_match(match_id: str, db: Session = Depends(get_db)):
    db_match = crud_match.delete_match(db, match_id=match_id)
    if db_match is None:
        raise HTTPException(status_code=404, detail="Match not found")
    return db_match
