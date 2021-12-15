from pydantic import BaseModel

class User_creation(BaseModel):
    name:str
    email: str
    password: str
    mobile:int