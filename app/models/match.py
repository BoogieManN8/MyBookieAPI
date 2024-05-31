from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base
from datetime import datetime
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

    logs = relationship("Log", back_populates="match")
