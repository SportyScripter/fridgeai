from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float
from pydantic import BaseModel
from db.base_class import Base
from sqlalchemy.sql import func

class Product(Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    quantity = Column(Float, nullable=False)
    unit = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    class Config:
        orm_mode = True

class ProductCreate(BaseModel):
    name : str
    quantity : float
    unit : str

class PrductDelete(BaseModel):
    name: str

