from sqlalchemy import Column, Float, Integer, String, TIMESTAMP
from sqlalchemy.sql.expression import text

from app.database import Base

class Products(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(length=20), nullable=False, unique=True)
    price = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    description = Column(String, nullable=True)
    created_on = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    stock = Column(Integer, nullable=False)

class Customer(Base):
    __tablename__ = "customer"
    id = Column(Integer, primary_key=True, nullable=False)
    full_name = Column(String, nullable=False)
    username = Column(String(length=20), nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    address = Column(String)
    created_on = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    
class Vendor(Base):
    __tablename__ = "vendor"
    id = Column(Integer, primary_key=True, nullable=False)
    full_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone_number = Column(String, nullable=False)
    password = Column(String, nullable=False)
    address = Column(String)
    created_on = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))