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

class UserWithComment(User):
    comment: Optional[str] = None
    class Config:
        from_attributes = True

class UserDetailResponse(BaseModel):
    message: str
    user: UserWithComment
    class Config:
        from_attributes = True
