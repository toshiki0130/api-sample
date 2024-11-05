from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker
from app.config.base import settings

def init_connection():
    db_config = {
        "pool_size": 5,
        "max_overflow": 10,
        "pool_recycle": 300,
        "pool_pre_ping": True,
        "pool_timeout": 30
    }
    pool = create_engine(
        URL.create(
            drivername="postgresql",
            username=settings.DB_USER,
            password=settings.DB_PASS,
            host=settings.DB_HOST,
            port=settings.DB_PORT,
            database=settings.DB_NAME
        ),
        **db_config
    )
    return pool
engine = init_connection()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 