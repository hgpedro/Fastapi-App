from fastapi import Form
from pydantic import BaseModel, ConfigDict, EmailStr, conint
from datetime import datetime
from typing import Optional, Union

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        from_attributes = True

class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    email: EmailStr 
    password: str 


class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    
    acess_token: str
    token_type: str

class TokenData(BaseModel):
    model_config = ConfigDict(coerce_numbers_to_str=True)
    id: Optional[str] = None

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1) # type: ignore