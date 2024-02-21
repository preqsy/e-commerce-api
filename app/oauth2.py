from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from app.config import settings


from schemas.custom_schemas import TokenData


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def create_access_token(data:dict):
    data_to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.EXPIRY_TIME)
    data_to_encode.update({"exp": expire})
    access_token = jwt.encode(data_to_encode, settings.SECRET_KEY, settings.ALGORITHM)
    return access_token

def verify_access_token(token, credentials_exception):
    try:
        payload = jwt.decode(token=token, key=settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        id = payload.get("user_id")
        if id is None:
            raise credentials_exception
        token_data = TokenData(id=id)
    except JWTError:
        raise credentials_exception
    return token_data
def get_current_user(
    token = Depends(oauth2_scheme)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Could'nt validate credential",
        headers={"WWW-Authenticate": "Bearer"},
    )
    verify_access_token(
        token=token, credentials_exception=credentials_exception
    )
