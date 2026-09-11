from sqlalchemy import Column, Integer, String

from database import Base


# This class represents an actual table in Postgres, not a request shape
class Student(Base):
    __tablename__ = "students"  # the actual table name inside Postgres

    id = Column(Integer, primary_key=True, index=True)  # auto-incrementing unique ID
    name = Column(String, nullable=False)  # nullable=False = required, can't be empty
    intra_login = Column(String, unique=True, nullable=False)  # unique = no two students can share a login