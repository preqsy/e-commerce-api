from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from schemas.products import ProductCreate, ProductReturn, ProductUpdate
from app import models
from typing import List

router = APIRouter(prefix="/users")

@router.post("/")
def create_users(user:UserCreate, db:Session = Depends(get_db)):
    pass