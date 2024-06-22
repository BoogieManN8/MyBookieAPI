from sqlalchemy.orm import Session
from app.models.match import Match
from app.schemas.match import MatchCreate, MatchUpdate
from app.models.log import Log
import logging


def get_match(db: Session, match_id: str):
    return db.query(Match).filter(Match.id == match_id).first()

def get_matches(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Match).offset(skip).limit(limit).all()

def get_user_matches(db: Session, user_id: str, skip: int = 0, limit: int = 10):
    return db.query(Match).filter(Match.user_id == user_id).offset(skip).limit(limit).all()

def create_match(db: Session, match: MatchCreate):
    try:
        logging.info(f"Creating match with data: {match.dict()}")
        db_match = Match(**match.dict(exclude={'logs'}))
        db.add(db_match)
        db.commit()
        db.refresh(db_match)
        
        if match.logs:
            logging.info(f"Adding logs for match id: {db_match.id}")
            for log in match.logs:
                log_data = log.dict()
                log_data['match_id'] = db_match.id
                logging.info(f"Creating log with data: {log_data}")
                db_log = Log(**log_data)
                logging.info(f"Adding log: {db_log}")
                db.add(db_log)
            db.commit()

        return db_match
    except Exception as e:
        logging.error(f"Error creating match: {str(e)}")
        raise e

def update_match(db: Session, match_id: str, match: MatchUpdate):
    db_match = get_match(db, match_id)
    if db_match is None:
        return None
    
    update_data = match.dict(exclude_unset=True, exclude={"logs"})
    
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
