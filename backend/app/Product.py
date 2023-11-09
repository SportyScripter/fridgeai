from pydantic import BaseModel, ValidationError
from Category import Category



class Product(BaseModel):
    name: str | None
    price: float | None
    quantity: int | None
    weight: float | None
    product_category: Category | None

