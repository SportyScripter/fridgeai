from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

import database as db


class User(db.Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    # products = relationship("Product", back_populates="owner")


class Product(db.Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Integer)
    quantity = Column(Integer)
    unit = Column(String)
    # owner_id = Column(Integer, ForeignKey("users.id"))

    # owner = relationship("User", back_populates="products")
