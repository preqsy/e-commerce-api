from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app import models
from app.utils import verify
from app.oauth2 import create_access_token
from schemas.users import AuthUserUpdate


router = APIRouter(tags=["Authentication"])

@router.post("/auth/login")
def auth_user(user:OAuth2PasswordRequestForm = Depends(), db:Session=Depends(get_db)):
    user_details = db.query(models.AuthUser).filter(models.AuthUser.email == user.username).first()
    if not user_details:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid username"
        )
    if not verify(hashed_password=user_details.password, new_password=user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid password"
        )
    access_token = create_access_token(
        {"user_id": user_details.id}
    )
    return {"access_token" : access_token, "token_type" : "bearer"}