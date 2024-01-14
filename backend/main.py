from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from pathlib import Path
from core.config import config
from db.session import engine, db, SessionLocal
from db.models import product
from sqlalchemy.orm import Session
from db.base_class import Base

env_path = Path('.') / '.env'
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
    products = db.query(product.Product).all()
    if not products:
        raise HTTPException(status_code=404, detail="No products found")
    return products

@app.post("/product/create")
def create_product(product_data: product.ProductCreate, db: Session = Depends(get_db)):
    db_product = product.Product(**product_data.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@app.delete("/product/delete/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product_to_delete = db.query(product.Product).filter_by(id=product_id).first()
    if product_to_delete:
        db.delete(product_to_delete)
        db.commit()
        return {f'Product: nr: {product_id} deleted successfully': product_to_delete.name}
    raise HTTPException(status_code=404, detail="Product not found")
