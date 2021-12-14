from pydantic import BaseModel

class User_creation(BaseModel):
    email: str
    password: str
    mobile:int