from typing import Optional
from pydantic import BaseModel

class UserBase(BaseModel):
    user_id: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    nickname: Optional[str] = None
    class Config:
        from_attributes = True

