from pydantic import BaseModel
from typing import Optional
from enum import Enum

class LogType(str, Enum):
    RED = "Red Card"
    YELLOW = "Yellow Card"
    PENALTY = "Penalty"
    THROW = "Throw in"
    GOAL = "Goal"

class LogBase(BaseModel):
    log_type: LogType
    team: int
    time: float
    half: int

class LogCreate(LogBase):
    pass

class LogUpdate(LogBase):
    pass

class LogInDBBase(LogBase):
    id: str
    match_id: Optional[str] = None

    class Config:
        orm_mode = True

class Log(LogInDBBase):
    pass

class LogInDB(LogInDBBase):
    pass
