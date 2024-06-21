from sqlalchemy.orm import Session
from app.models.match import Match
from app.schemas.match import MatchCreate, MatchUpdate

def get_match(db: Session, match_id: str):
    return db.query(Match).filter(Match.id == match_id).first()

def get_matches(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Match).offset(skip).limit(limit).all()

def get_user_matches(db: Session, user_id: str, skip: int = 0, limit: int = 10):
    return db.query(Match).filter(Match.user_id == user_id).offset(skip).limit(limit).all()

def create_match(db: Session, match: MatchCreate):
    # Create the match
    db_match = Match(
        **match.dict(exclude={"logs"})
    )
    db.add(db_match)
    db.commit()
    db.refresh(db_match)

    # Add logs if any
    if match.logs:
        for log in match.logs:
            db_log = Log(
                **log.dict(), match_id=db_match.id
            )
            db.add(db_log)
        db.commit()

    return db_match

def update_match(db: Session, match_id: str, match: MatchUpdate):
    db_match = get_match(db, match_id)
    if db_match is None:
        return None
    update_data = match.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_match, key, value)
    db.commit()
    db.refresh(db_match)
    return db_match

def delete_match(db: Session, match_id: str):
    db_match = get_match(db, match_id)
    if db_match is None:
        return None
    db.delete(db_match)
    db.commit()
    return db_match
