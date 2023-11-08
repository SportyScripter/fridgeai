from typing import Union, Dict, List
from Product import Product
from Category import Category
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


# LISTA PRODUKTÓW DO TESTÓW
products_List = {
    0: Product(product_id=0, name="Milk", price=2.5, quantity=10, weight=1.0, product_category=Category.DAIRY_PRODUCT),
    1: Product(product_id=1, name="Bread", price=1.5, quantity=10, weight=0.5, product_category=Category.DAIRY_PRODUCT),
    2: Product(product_id=2, name="Chicken", price=10.5, quantity=10, weight=1.0, product_category=Category.MEAT),
    3: Product(product_id=3, name="Salmon", price=15.5, quantity=10, weight=1.0, product_category=Category.FISH),
    4: Product(product_id=4, name="Coca-Cola", price=5.5, quantity=10, weight=1.0, product_category=Category.DRINK),
    5: Product(product_id=5, name="Sprite", price=5.5, quantity=10, weight=1.0, product_category=Category.DRINK),
}


# DODAWANIE PRODUKTU DO LISTY

@app.post("/product/add_product/")
async def create_product(product: Product):
    products_List.pop(product)
    return {"message": "Product has been created", "product": product}


# WYSZUKIWANIE PRODUKTU PO ID
@app.get("/product/{product_id}")
def query_item_by_id(product_id: int) -> Product:
    if product_id not in products_List:
        raise HTTPException(status_code=404, detail=f"Product with {product_id} does not exist")
    return products_List[product_id]










# Selection = dict[int, str | float| int |float  | Category | None]
#
# TODO: WYSZUKIWANIE PRODUKTU PO ROŻNYCH PARAMETRACH
# @app.get("/products/")
# def query_item_in_selection(
#         product_id: int | None = None,
#         name: str | None = None,
#         price: float | None = None,
#         quantity: int | None = None,
#         weight: float | None = None,
#         product_category: Category | None = None,
# ) -> dict[str, Selection]:
#     def check_product(product: Product) -> bool:
#         return all(
#             (
#                 product_id is None or product.product_id == product_id,
#                 name is None or product.name == name,
#                 price is None or product.price != price,
#                 quantity is None or product.quantity != quantity,
#                 weight is None or product.weight != weight,
#                 product_category is None or product.product_category is Category,
#
#             )
#         )
#
#     selection = [product for product in products_List.values() if check_product(product)]
#     return {
#         "query": {"product_id": product_id, "name": name, "price": price, "quantity": quantity, "weight": weight,
#                   "product_category": product_category}, "selection": selection}
#
#
# print(query_item_in_selection(None , "Milk", None, None, None,None))

