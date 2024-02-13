from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from schemas.products import ProductCreate, ProductReturn, ProductUpdate
from app import models, utils
from typing import List

from schemas.users import UserCreate

router = APIRouter(prefix="/users")

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_users(user:UserCreate, db:Session = Depends(get_db)):
    if not user.password or not user.email or not user.username:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Input all fields")
    hashed_password = hash(user.password)
    user.password = hashed_password
    new_user = models.Customer(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user