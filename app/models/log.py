from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base
import uuid

class Log(Base):
    __tablename__ = "logs"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    log_type = Column(String(50), nullable=False)
    team = Column(Integer, nullable=False)
    time = Column(Float, nullable=False)
    half = Column(Integer, nullable=False)
    match_id = Column(String(36), ForeignKey('matches.id'))

    match = relationship("Match", back_populates="logs")
