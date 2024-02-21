from fastapi import APIRouter, Depends, status, HTTPException, Header
from sqlalchemy.orm import Session
from app.database import get_db
from app.oauth2 import get_current_auth_user
from schemas.products import ProductCreate, ProductReturn, ProductUpdate
from app import models
from app.models import *
from typing import Annotated, List, Optional
router = APIRouter(prefix="/products")

@router.get("/", response_model=List[ProductReturn])
def get_all_products(db:Session = Depends(get_db),current_user=Depends(get_current_auth_user)):
    print(current_user.id)
    all_products = db.query(models.Products).all()
    if all_products == []:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"no products")
    return all_products

@router.get("/{id}", response_model=ProductReturn)
def get_single_product(id: int, db:Session = Depends(get_db)):
    single_product = db.query(models.Products).filter(models.Products.id == id).first()
    if not single_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"product with id: {id} doesn't exist")
    return single_product

@router.post("/", status_code=status.HTTP_201_CREATED)
def get_products(product:ProductCreate, db:Session = Depends(get_db),current_user:int=Depends(get_current_auth_user)):
    new_product = models.Products(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

    
@router.put("/{id}", response_model=ProductReturn)
def update_product(id:int, product:ProductUpdate, db:Session = Depends(get_db)):
    updated_product = db.query(models.Products).filter(models.Products.id == id)
    if not updated_product.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"product with id: {id} doesn't exist")
    updated_product.update(product.dict(), synchronize_session=False)
    db.commit()
    return updated_product.first()

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(id:int, db:Session = Depends(get_db)):
    product_query = db.query(models.Products).filter(models.Products.id == id)
    if not product_query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"product with id: {id} doesn't exist")
    product_query.delete(synchronize_session=False)
    db.commit()
    

