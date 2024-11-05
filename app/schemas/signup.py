from pydantic import BaseModel
from .users import User

class Signup(BaseModel):
    user_id: str
    nickname: str

class SignupResponse(BaseModel):
    message: str
    user: User
    class Config:
        from_attributes = True

