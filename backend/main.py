from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from pathlib import Path
from db.models import user
from passlib.handlers.bcrypt import bcrypt
from core.config import config
from db.session import engine, db, SessionLocal
from db.models import product
from sqlalchemy.orm import Session
from db.base_class import Base
from sqlalchemy.exc import IntegrityError
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

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

@app.delete("/product/delete")
def delete_product(product_delete: product.PrductDelete, db: Session = Depends(get_db)):
    product_to_delete = db.query(product.Product).filter_by(name=product_delete.name).first()
    if product_to_delete:
        db.delete(product_to_delete)
        db.commit()
        return {f'Product: {product_delete} deleted successfully': product_to_delete}
    raise HTTPException(status_code=404, detail="Product not found")

@app.post("/register/")
def register(username: str, email: str, password: str, db: Session = Depends(get_db)):
    try:
        db_user = user.User(username=username, email=email, hashed_password=bcrypt.hash(password))
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return {'message': 'User created successfully'}
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail='Username or email already registered')

password_hasher = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/token")
def login(username: str, password: str, db: Session = Depends(get_db)):
    check_user = db.query(user.User).filter(user.User.username == username).first()
    if not check_user or not password_hasher.verify(password, check_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {'access_token': username, 'token_type': 'bearer','message': 'Logged in successfully'}




