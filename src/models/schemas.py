from pydantic import BaseModel
from typing import Optional

class User_creation(BaseModel):
    name:str
    email: str
    password: str
    mobile:str

class Show_User(BaseModel):
    name:str
    email: str
    id:str
    class Config():
        orm_mode=True

class Login(BaseModel):
    username:str
    password:str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None