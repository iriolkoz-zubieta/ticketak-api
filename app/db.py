"""Datu-basearen konexioa eta saioen kudeaketa."""

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./tickets.db")

connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(DATABASE_URL, connect_args=connect_args, future=True)
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
    future=True,
)


class Base(DeclarativeBase):
    """Proiektuaren modelo guztien oinarria."""


def get_db():
    """FastAPIren dependendentzia: saio bat ireki eta beti itxi."""

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
