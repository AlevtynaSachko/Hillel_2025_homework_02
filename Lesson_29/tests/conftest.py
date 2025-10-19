import pytest
from sqlalchemy import text
from src.db import Base, engine, SessionLocal, wait_for_db

@pytest.fixture(scope="session", autouse=True)
def _ensure_db_ready():
    wait_for_db()
    Base.metadata.create_all(bind=engine)
    yield
    with engine.begin() as conn:
        conn.execute(text("DROP TABLE IF EXISTS items CASCADE;"))

@pytest.fixture()
def db():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
