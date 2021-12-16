from typing import List
from fastapi import APIRouter,status,Depends,HTTPException
import models.schemas,models.models,models.database
from sqlalchemy.orm import Session
from passlib.hash import bcrypt

router=APIRouter()

get_db=models.database.get_db

@router.post('/user/signin',status_code=status.HTTP_201_CREATED)
def new_user(req:models.schemas.User_creation,db: Session=Depends(get_db)):
    h_p= bcrypt.hash("req.password")
    h_m= bcrypt.hash("req.mobile")
    new_user=models.models.User(name=req.name,email=req.email,password=h_p,mobile=h_m)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/user',status_code=status.HTTP_200_OK,response_model=List[models.schemas.Show_User])
def show_all(db: Session=Depends(get_db)):
    users=db.query(models.models.User).all()
    return users

@router.get('/user/{id}',status_code=status.HTTP_200_OK,response_model=models.schemas.Show_User)
def show_single_user(id,db: Session=Depends(get_db)):
    user=db.query(models.models.User).filter(models.models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with id {id} is not available")

    return user