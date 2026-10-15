import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm
import os

#DATABASE_URL = "postgresql://myuser:password@localhost:5432/fastapi_database"

DATABASE_URL = os.getenv("DATABASE_URL","postgresql+psycopg://myuser:password@localhost:5432/fastapi_database")

if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql+psycopg://", 1)

engine = _sql.create_engine(DATABASE_URL)

SessionLocal = _orm.sessionmaker(autocommit = False, autoflush = False , bind = engine)

Base = _declarative.declarative_base()

