from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    apple_token: str
    push_token: str
    is_guest: bool

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class UserInDBBase(UserBase):
    id: str
    created_at: datetime

    class Config:
        orm_mode = True

class User(UserInDBBase):
    pass

class UserInDB(UserInDBBase):
    pass
