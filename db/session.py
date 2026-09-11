from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from core.config import settings

engine = create_engine(settings.database_url, pool_pre_ping=True, pool_size=settings.db_pool_size,
    max_overflow=settings.db_max_overflow, pool_timeout=settings.db_pool_timeout, pool_recycle=settings.db_pool_recycle,
    echo=settings.db_echo, )

SessionLocal = sessionmaker(bind=engine, class_=Session, autoflush=False, autocommit=False, expire_on_commit=False, )


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()

    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
