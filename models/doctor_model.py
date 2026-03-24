from sqlalchemy import Column, Integer, String
from database.database import Base

class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    specialization = Column(String(50))