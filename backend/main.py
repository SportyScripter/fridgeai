import os
import json
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from pathlib import Path
from core.config import config
from db.session import engine, SessionLocal
from db.models import product, recipe
from sqlalchemy.orm import Session
from db.base_class import Base
from openai import OpenAI

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)
env_path = Path(".") / ".key.env"
load_dotenv(dotenv_path=env_path)


def create_tables():
    try:
        Base.metadata.create_all(bind=engine)
        print("Tables created successfully.")
    except Exception as e:
        print("Error creating tables:", e)


def start_application():
    app = FastAPI(title=config.PROJECT_NAME, version=config.PROJECT_VERSION)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    create_tables()
    return app


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = start_application()


@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    return db.query(product.Product).all()


@app.get("/recipes")
def get_products(db: Session = Depends(get_db)):
    return db.query(recipe.Recipe).all()


@app.post("/product/create")
def create_product(product_data: product.ProductCreate, db: Session = Depends(get_db)):
    db_product = product.Product(**product_data.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


@app.delete("/product/delete/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    if product_to_delete := db.query(product.Product).filter_by(id=product_id).first():
        db.delete(product_to_delete)
        db.commit()
        return {
            f"Product no: {product_id} deleted successfully": product_to_delete.name
        }
    raise HTTPException(status_code=404, detail="Product not found")


@app.delete("/recipe/delete/{recipe_id}")
def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):
    if recipe_to_delete := db.query(recipe.Recipe).filter_by(id=recipe_id).first():
        db.delete(recipe_to_delete)
        db.commit()
        return {f"Recipe no: {recipe_id} deleted successfully": recipe_to_delete.name}
    raise HTTPException(status_code=404, detail="Recipe not found")


@app.post("/recipe/create")
def create_recipe(db: Session = Depends(get_db)):
    products = db.query(product.Product).all()

    api_key = os.getenv("api_key")
    client = OpenAI(api_key=api_key)

    prompt = "W mojej lodówce znajdują się: "
    for item in products:
        prompt += f"{item.name} - {item.quantity} {item.unit}, "
    prompt += 'stwórz z tego dokładny przepis. Nie posiadam innych składników, jeżeli nie jesteś w stanie stworzyć z tego przepisu poinformuj usera o tym. Przepis zwróć w formie JSON w strukturze {"name": <nazwa przepisu>, "description": <opis dania i dokładny przepis>}. Nie zwracaj nic poza obiektem JSON. Jeśli nie jesteś w stanie stworzyć przepisu z podanych skłądników zwróć stosowną informację w formacie {"error": <treść błędu>}.'

    print("Prompt:", prompt)

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}]
    )

    print("Completion", completion)

    response = dict(json.loads(completion.choices[0].message.content))

    if "error" in response:
        raise HTTPException(status_code=400, detail=response["error"])

    db_recipe = recipe.Recipe(**response)
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)

    return response
