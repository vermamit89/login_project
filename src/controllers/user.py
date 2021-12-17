from fastapi import Depends,status,HTTPException
from ..models import schemas,database,models
from sqlalchemy.orm import Session
from passlib.hash import bcrypt
import uuid
import yagmail

get_db=database.get_db


def create_user(req:schemas.User_creation,db: Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.email==req.email).first()
    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f'User record already exist!!!')
    u_id=uuid.uuid4()
    h_p= bcrypt.hash(req.password)
    h_m= bcrypt.hash(req.mobile)
    new_user=models.User(name=req.name,email=req.email,password=h_p,
                                 mobile=h_m,isVerified=False,uniqueId=str(u_id))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    yag = yagmail.SMTP("vermatest1@gmail.com",'Test@Verma2')
    contents = ['http://localhost:3000/verify/' + new_user.uniqueId]
    yag.send(new_user.email, 'Verify-Email', contents)

    return new_user




def show_all(db: Session=Depends(get_db)):
    users=db.query(models.models.User).all()
    return users

def show_1(id:int, db: Session=Depends(get_db)):
    user=db.query(models.models.User).filter(models.models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} is not available")
    elif user.isVerified == False:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} is not verified")

    return user

