from pydantic import BaseModel

class User_creation(BaseModel):
    name:str
    email: str
    password: str
    mobile:int

class Show_User(BaseModel):
    name:str
    email: str
    class Config():
        orm_mode=True

class Login(BaseModel):
    username:str
    password:str