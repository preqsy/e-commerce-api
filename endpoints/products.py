from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from schemas.products import ProductCreate
from app import models

router = APIRouter(prefix="/products")


@router.post("/")
def get_products(product:ProductCreate, db:Session = Depends(get_db)):
    new_product = models.Products(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product