from fastapi import Depends,status,HTTPException
import models.schemas,models.database,models.models
from sqlalchemy.orm import Session
from passlib.hash import bcrypt

get_db=models.database.get_db


def create(req:models.schemas.User_creation,db: Session=Depends(get_db)):
    h_p= bcrypt.hash(req.password)
    h_m= bcrypt.hash(req.mobile)
    new_user=models.models.User(name=req.name,email=req.email,password=h_p,mobile=h_m)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show_all(db: Session=Depends(get_db)):
    users=db.query(models.models.User).all()
    return users

def show_1(id:int, db: Session=Depends(get_db)):
    user=db.query(models.models.User).filter(models.models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with id {id} is not available")

    return user

