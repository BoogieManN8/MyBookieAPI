from sqlalchemy import Column, String, Boolean, DateTime
from app.db.base import Base
from datetime import datetime
import uuid

class User(Base):
    __tablename__ = "users"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    apple_token = Column(String(255), nullable=False)
    push_token = Column(String(255), nullable=False)
    is_guest = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
