# from typing import List
from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    quantity: int
    unit: str


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    # owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    # products: List[Product] = []

    class Config:
        orm_mode = True
