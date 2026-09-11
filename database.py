from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# This matches the values we set when starting the Docker container:
# POSTGRES_PASSWORD=postgres, POSTGRES_DB=achievements, port 5432
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/achievements"

engine = create_engine(DATABASE_URL)

# SessionLocal is a "factory"
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# SQLAlchemy uses this to know "these Python classes represent database tables."
Base = declarative_base()


def get_db():
    """
    A FastAPI dependency: opens a session, hands it to the route function
    via 'yield', then always closes it afterward — even if the route
    raises an error. FastAPI calls this automatically when a route
    uses Depends(get_db).
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()