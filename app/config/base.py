from pydantic import field_validator
from pydantic_settings import BaseSettings
from typing import List, Union
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):

    IS_LOCAL: bool = True
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "FastAPI"
    BACKEND_CORS_ORIGINS: List[str] = []

    @field_validator("BACKEND_CORS_ORIGINS", mode="before")
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str):
            return [i.strip() for i in v.split(",")]
        return v

    # For DB
    DB_HOST: str
    DB_PORT: str
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

settings = Settings()