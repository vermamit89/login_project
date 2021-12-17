from typing import List
from fastapi import APIRouter,status,Depends
from fastapi.security import oauth2
from sqlalchemy import schema
from ..models import schemas,models,database
from sqlalchemy.orm import Session
from ..controllers import user
from ..routes import oauth2

router=APIRouter(
       prefix='/user',
       tags=['User']
)

get_db=database.get_db

@router.post('/signup',status_code=status.HTTP_201_CREATED,response_model=schemas.Show_User)
def new_user(req:schemas.User_creation,db: Session=Depends(get_db)):
    return user.create_user(req,db)

# @router.get('/',status_code=status.HTTP_200_OK,response_model=List[models.schemas.Show_User])
# def show_all(db: Session=Depends(get_db)):
#     return user.show_all(db)

@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=schemas.Show_User)
def show_single_user(id,db: Session=Depends(get_db), get_current_user: schemas.Show_User =  Depends(oauth2.get_current_user)):
    return user.show_1(id,db)