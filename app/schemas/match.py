from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional
from app.schemas.log import Log

class MatchBase(BaseModel):
    team1: str
    team2: str
    team1_name: str
    team2_name: str
    halves: int
    half_times: int
    date: datetime
    is_favourite: bool
    current_time: int

class MatchCreate(MatchBase):
    user_id: str  # Add user_id to the creation schema

class MatchUpdate(MatchBase):
    logs: Optional[List[Log]] = []

class MatchInDBBase(MatchBase):
    id: str
    user_id: str  # Add user_id to the database schema

    class Config:
        orm_mode = True

class Match(MatchInDBBase):
    logs: List[Log]

class MatchInDB(MatchInDBBase):
    pass
