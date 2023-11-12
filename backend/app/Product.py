import pydantic
class Product(pydantic.BaseModel):
    id: int
    name: str
    quantity: int
    categories: str

