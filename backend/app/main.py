from typing import Union, Dict, List

from starlette import schemas

from Product import Product
from Category import Category
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# LISTA PRODUKTÓW DO TESTÓW
products_List: Dict[int, Product] = {
    0: Product(name="Milk", price=2.5, quantity=10, weight=1.0, product_category=Category.DAIRY_PRODUCT),
    1: Product(name="Bread", price=1.5, quantity=10, weight=0.5, product_category=Category.DAIRY_PRODUCT),
    2: Product(name="Chicken", price=10.5, quantity=10, weight=1.0, product_category=Category.MEAT),
    3: Product(name="Salmon", price=15.5, quantity=10, weight=1.0, product_category=Category.FISH),
    4: Product(name="Coca-Cola", price=5.5, quantity=10, weight=1.0, product_category=Category.DRINK),
    5: Product(name="Sprite", price=5.5, quantity=10, weight=1.0, product_category=Category.DRINK),
}
#Zwraca wszystkie artykuły
@app.get("/products")
def getProducts():
    return products_List
# Zwaraca id ostatniego artykułu, potrzebne do dodawania nowego artykułu
@app.get("/last_id")
def getLastId():
    return max(products_List.keys())

#Dodaje nowy artykuł, nie trzeba podawać wszystkich parametrów, wystarczy jeden ale musi być zgodny z typem a pozostałe parametry muszą być None
@app.get("/")
def createProduct(
        name: str | None = None,
        price: float | None = None,
        quantity: int | None = None,
        weight: float | None = None,
        product_category: Category | None = None):
    tempProduct = Product(
        name=name,
        price=price,
        quantity=quantity,
        weight=weight,
        product_category=product_category
    )
    products_List[getLastId()] = tempProduct
    return products_List





