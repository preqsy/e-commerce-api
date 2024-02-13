from typing import Optional
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    username: str
    address : Optional[str] = None