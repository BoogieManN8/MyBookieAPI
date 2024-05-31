from pydantic import BaseModel
from typing import Optional
from app.models.log import LogType

class LogBase(BaseModel):
    log_type: LogType
    team: int
    time: float
    half: int

class LogCreate(LogBase):
    match_id: str

class LogUpdate(LogBase):
    pass

class LogInDBBase(LogBase):
    id: str

    class Config:
        from_attributes = True

class Log(LogInDBBase):
    pass

class LogInDB(LogInDBBase):
    pass
