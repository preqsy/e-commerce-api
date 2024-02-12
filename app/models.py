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
    # features = Column(List)