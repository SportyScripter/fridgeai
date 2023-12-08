from fastapi import FastAPI, APIRouter, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from pathlib import Path
from core.config import config
from db.session import engine, db, SessionLocal, Base
from db.models import product



env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


def create_tables():
	Base.metadata.create_all(bind=engine)     

def start_application():
   app = FastAPI(title=config.PROJECT_NAME,version=config.PROJECT_VERSION)
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
def get_products():
   list = db.query(product.Product).all()

   if list is None:
      return {"message": "No products found"}
   
   return list

@app.post("/product/create")
async def create_product(product_create: product.ProductBase):
   list = db.query(product.Product).all()
   for i in list:
      if product_create.name == i.name:
         raise HTTPException(status_code=406, detail="Product already exists, please update your product")
   db_product = product.Product(name=product_create.name, quantity=product_create.quantity, unit=product_create.unit)
   db.add(db_product)
   db.commit()
   db.refresh(db_product)
   return {f'Product: {product_create} added succesfully': db_product}

@app.delete("/product/delete")
async def delete_product(product_delete: product.PrductDelete):
   list = db.query(product.Product).all()
   for i in list:
      if product_delete.name == i.name:
         db.delete(i)
         db.commit()
         return {f'Product: {product_delete} deleted succesfully': i}
   raise HTTPException(status_code=404, detail="Product not found")