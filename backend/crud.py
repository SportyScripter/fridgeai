from sqlalchemy.orm import Session

import models, schemas
import helper


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()


def create_product(db: Session, product: schemas.ProductCreate):
    p = models.Product(name=product.name, quantity=product.quantity, unit=product.unit)

    db.add(p)
    db.commit()
    db.refresh(p)

    return p


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = helper.get_hashed_password(plain_text_password=user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user
