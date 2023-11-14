from fastapi import FastAPI

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
    create_tables()
    return app


app = start_application()

#Creating a cursor object using the cursor() method
@app.get("/products")
def get_products():
   return db.query(Product).all()

# @app.get("/pure_list")
# def get_List():
#    cursor.execute('''SELECT * from Products''')
#    result = cursor.fetchall()
#    return result
