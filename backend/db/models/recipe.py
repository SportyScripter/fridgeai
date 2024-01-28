from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float
from pydantic import BaseModel
from db.base_class import Base
from sqlalchemy.sql import func


class Recipe(Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now())

    class Config:
        orm_mode = True


class RecipeCreate(BaseModel):
    name: str
    description: str


class PrductDelete(BaseModel):
    id: int
