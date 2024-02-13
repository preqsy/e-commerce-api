from typing import ClassVar
from pydantic import BaseModel, constr, root_validator
from enum import Enum

class ProductCategoriesEnum(str, Enum):
    VEHICLES = "vehicles"
    PROPERTY = "property"
    HEALTH = "health"
    FASHION = "fashion"
    PETS = "pets"
    BABIES = "babies"
    FOOD = "foods"
    AGRICULTURE = "agriculture"
    SPORTS = "sports"
    SERVICES = "services"
    ELECTRONICS = "electronics"
    PHONES = "phones"

class ProductCreate(BaseModel):
    CATEGORY: ClassVar[str] = "category"
    name: constr(to_lower=True)
    description:str
    price:float
    stock : int
    category:ProductCategoriesEnum
class ProductUpdate(BaseModel):
    name: constr(to_lower=True)
    description:str
    price:float
    stock: int
class ProductReturn(BaseModel):
    name: str
    description:str
    price:float
    stock: int
    category:str
    
