from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
import database as db_import

models.db.Base.metadata.create_all(bind=db_import.engine)

app = FastAPI()


# Dependency
def get_db():
    db = db_import.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    if db_user := crud.get_user_by_email(db, email=user.email):
        raise HTTPException(status_code=400, detail="Email already registered.")

    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_users(db, skip=skip, limit=limit)


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    if db_user := crud.get_user(db, user_id=user_id):
        return db_user
    else:
        raise HTTPException(status_code=404, detail="User not found.")


@app.get("/products/", response_model=List[schemas.Product])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_products(db, skip=skip, limit=limit)


@app.post("/products/", response_model=schemas.Product)
def read_products(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product=product)
