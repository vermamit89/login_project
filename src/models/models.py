from sqlalchemy import Column,Integer,String
# from sqlalchemy.engine.base import Transaction
from . database import base


class User(base):
    __tablename__='User'

    id=Column(Integer,primary_key=True,index=True)
    email=Column(String)
    password=Column(String)
    mobile=Column(Integer)

