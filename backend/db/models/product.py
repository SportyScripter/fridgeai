from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float

from db.base_class import Base

class Product(Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    quantity = Column(Float, nullable=False)
    unit = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
