
""" There are only 2 roles(Authors and Admin) any user that signups immediately becomes an Author, we are going to implement likes and sharing of posts, also search by POST TITLE, TAGS & CATEGORIES, AUTHOR """

from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, EmailStr

class Interest(Enum):
    TECH = "tech"
    PHOTOGRAPHY = "photography"
    ART = "art"
    
class Category(Enum):
    TECH = "tech"
    PHOTOGRAPHY = "photography"
    ART = "art"
    
class Tag(Enum):
    TECH = "tech"
    PHOTOGRAPHY = "photography"
    ART = "art"

class AuthorSchema(BaseModel):
    id : int
    full_name: str
    username: str
    email: EmailStr
    password: str
    interest: Optional[Interest]
    bio: str
    
class PostSchema(BaseModel):
    id:int
    title:str
    description:Optional[str]
    body:str
    image_field: "image"
    published_time: datetime
    author_id:int
    last_updated_time: datetime
    status: bool
    category: Category
    tag: Tag
    
class Comment(BaseModel):
    id:int
    post_id:PostSchema.id
    user_id:AuthorSchema.id
    body:str
    comment_time: datetime
    
class Likes(BaseModel):
    """Both primary keys"""
    post_id:PostSchema.id
    user_id:AuthorSchema.id
    
class NewLetter(BaseModel):
    email: str
    
    

    