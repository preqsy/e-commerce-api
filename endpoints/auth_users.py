from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from schemas.products import ProductCreate, ProductReturn, ProductUpdate
from app import models, utils
from typing import List

from schemas.users import AuthUserCreate, AuthUserUpdate

router = APIRouter(prefix="/auth")

@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=AuthUserUpdate)
def create_users(user:AuthUserCreate, db:Session = Depends(get_db)):
    if not user.password or not user.email or not user.username:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Input all fields")
    hashed_password = utils.hash_password(user.password)
    print(hashed_password)
    user.password = hashed_password
    new_user = models.AuthUser(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.put("/update-me")
def update_auth_user(auth_user:AuthUserUpdate, db:Session = Depends(get_db)):
    user = db.query(models.AuthUser)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id: {auth_user.id} doesn't exist")
    user.update(auth_user.dict(), synchronize_session=False)
    db.commit()
    return user.first()
    