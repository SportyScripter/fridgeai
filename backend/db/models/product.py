from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float
from pydantic import BaseModel

from db.base_class import Base

class Product(Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    quantity = Column(Float, nullable=False)
    unit = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S"))
    class Config:
        orm_mode = True

class ProductBase(BaseModel):
    name: str
    quantity: float
    unit: str

class ProductCreate(ProductBase):
    pass

class PrductDelete(ProductBase):
    pass

