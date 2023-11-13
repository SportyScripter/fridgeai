import pydantic
class Product(pydantic.BaseModel):
    name: str
    quantity: int
    weight: float


