from fastapi import FastAPI, status, HTTPException, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session # type: ignore
from app.config.base import settings
from app.api.main import api_router
from app.api import deps
from app import schemas
from app import crud

app = FastAPI(
    title = settings.PROJECT_NAME,
    openapi_url = f"{settings.API_V1_STR}/openapi.json"
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/signup", status_code=status.HTTP_201_CREATED, response_model=schemas.SignupResponse)
async def signup(*, db: Session = Depends(deps.get_db), obj: dict):
    if obj.get("user_id") is None or obj.get("password") is None:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content = {
                "message": "Account creation failed",
                "cause": "required user_id and password"
            }
        )
    
    if not (6 <= len(obj["user_id"]) <= 20 and 8 <= len(obj["password"]) <= 20):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content = {
                "message": "Account creation failed",
                "cause": "user_id must be between 6 and 20 characters, password must be between 8 and 20 characters"
            }
        )
    if not obj["user_id"].isalnum():
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content = {
                "message": "Account creation failed",
                "cause": "user_id must be alphanumeric"
            }
        )
    if not all(33 <= ord(char) <= 126 for char in obj["password"]):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "message": "Account creation failed",
                "cause": "password must contain only ASCII characters (excluding spaces and control characters)"
            }
        )
    if crud.get_user_by_user_id(session=db, user_id=obj["user_id"]):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content = {
                "message": "Account creation failed",
                "cause": "already same user_id is used"
            }
        )
    user = crud.create_user(session=db, user_create=obj)
    res = schemas.SignupResponse(
        message = "Account successfully created",
        user = schemas.User(
            user_id = user.user_id,
            nickname = user.user_id
        )
    )
    return res

app.include_router(api_router, prefix=settings.API_V1_STR)
