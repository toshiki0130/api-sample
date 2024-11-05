from sqlalchemy import Column, Integer, String
from .base import Base

class Users(Base):
    __tablename__ = "users"

    user_id = Column(String, primary_key=True)
    password = Column(String, nullable=False)
    nickname = Column(String, nullable=True)
    comment = Column(String, nullable=True)