from fastapi import APIRouter, Depends, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.api import deps
from app import crud, schemas

security = HTTPBasic()
router = APIRouter()

@router.get("/{user_id}")
async def read_user(
    *,
    db: Session = Depends(deps.get_db),
    user_id: str,
    credentials: HTTPBasicCredentials = Depends(security)
):
    if not credentials.username or not credentials.password:
        return JSONResponse(
            status_code = status.HTTP_401_UNAUTHORIZED,
            content = {
                "message": "Authentication failed"
            }
        )
    user_id_from_auth = credentials.username
    password_from_auth = credentials.password
    user = crud.get_user_by_user_id(session=db, user_id=user_id)
    if not user:
        return JSONResponse(
            status_code = status.HTTP_404_NOT_FOUND,
            content = {
                "message": "No User found"
            }
        )
    if user.user_id != user_id_from_auth or user.password != password_from_auth:
        return JSONResponse(
            status_code = status.HTTP_401_UNAUTHORIZED,
            content = {
                "message": "Authentication failed"
            }
        )
    return schemas.UserDetailResponse(
        message = "User details by user_id",
        user = schemas.UserWithComment(
            user_id = user.user_id,
            nickname = user.nickname if user.nickname else user.user_id,
            comment = user.comment if user.comment else None
        )
    )

@router.patch("/{user_id}")
async def update_user(
    *,
    db: Session = Depends(deps.get_db),
    user_id: str,
    credentials: HTTPBasicCredentials = Depends(security),
    obj: dict
):
  # ここまでしかできませんでした。
  pass

