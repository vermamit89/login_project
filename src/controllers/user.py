from fastapi import Depends,status,HTTPException
import models.schemas,models.database,models.models
from sqlalchemy.orm import Session
from passlib.hash import bcrypt
import uuid
import yagmail

get_db=models.database.get_db


def create_user(req:models.schemas.User_creation,db: Session=Depends(get_db)):
    u_id=uuid.uuid4()
    h_p= bcrypt.hash(req.password)
    h_m= bcrypt.hash(req.mobile)
    new_user=models.models.User(name=req.name,email=req.email,password=h_p,
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
                            detail=f"user with id {id} is not available")

    return user

