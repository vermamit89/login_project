from typing import List
from fastapi import APIRouter,status,Depends
import models.schemas,models.models,models.database
from sqlalchemy.orm import Session
import controllers.user

router=APIRouter(
       prefix='/user',
       tags=['User']
)

get_db=models.database.get_db

@router.post('/signup',status_code=status.HTTP_201_CREATED)
def new_user(req:models.schemas.User_creation,db: Session=Depends(get_db)):
    return controllers.user.create_user(req,db)

@router.get('/',status_code=status.HTTP_200_OK,response_model=List[models.schemas.Show_User])
def show_all(db: Session=Depends(get_db)):
    return controllers.user.show_all(db)

@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=models.schemas.Show_User)
def show_single_user(id,db: Session=Depends(get_db)):
    return controllers.user.show_1(id,db)