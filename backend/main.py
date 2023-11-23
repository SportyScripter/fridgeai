from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

from fastapi import FastAPI
from core.config import config
from db.session import engine, db
from db.base import Base, Product

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

app = start_application()

@app.get("/products")
def get_products():
   list = db.query(Product).all()

   if list is None:
      return {"message": "No products found"}
   
   return list
