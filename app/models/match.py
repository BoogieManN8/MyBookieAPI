from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
import uuid

class Match(Base):
    __tablename__ = "matches"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    team1 = Column(String(255), nullable=False)
    team2 = Column(String(255), nullable=False)
    team1_name = Column(String(255), nullable=False)
    team2_name = Column(String(255), nullable=False)
    halves = Column(Integer, nullable=False)
    half_times = Column(Integer, nullable=False)
    date = Column(DateTime, default=datetime.utcnow)
    is_favourite = Column(Boolean, default=False)
    current_time = Column(Integer, nullable=False)
    user_id = Column(String(36), ForeignKey('users.id'))

    user = relationship("User", back_populates="matches")
    logs = relationship("Log", back_populates="match", cascade="all, delete-orphan")


class MatchCreate(BaseModel):
    team1: str
    team2: str
    team1_name: str
    team2_name: str
    halves: int
    half_times: int
    date: Optional[datetime] = None
    is_favourite: Optional[bool] = None
    current_time: int
    user_id: Optional[str] = None
    logs: Optional[List[LogCreate]] = None