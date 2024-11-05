from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from app import models, schemas

def create_user(*, session: Session, user_create: schemas.UserCreate) -> models.Users:
    db_dict = jsonable_encoder(user_create)
    db_obj = models.Users(**db_dict)
    session.add(db_obj)
    return db_obj

def get_user_by_user_id(*, session: Session, user_id: str) -> models.Users:
    return session.query(models.Users).filter(models.Users.user_id == user_id).first()