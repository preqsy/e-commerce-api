from typing import Optional
from pydantic import BaseModel, EmailStr

from schemas.custom_schemas import PhoneNumber, Roles

class AuthUserCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    username: str
    address : Optional[str] = None
    default_role: Roles
    phone_number: str
    
class AuthUserUpdate(BaseModel):
    full_name: str
    email: EmailStr
    username: str
    address : Optional[str] = None
    default_role: Roles
    phone_number: str
class AuthUserUpdate(BaseModel):
    full_name: str
    email: EmailStr
    username: str
    address : Optional[str] = None
    default_role: Roles
    phone_number: str