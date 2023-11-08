from pydantic import BaseModel, ValidationError
from Category import Category

class Product(BaseModel):
    product_id: int
    name: str
    price: float
    quantity: int
    weight: float
    product_category: Category






