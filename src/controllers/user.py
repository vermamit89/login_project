from fastapi import Depends,status,HTTPException
from ..models import schemas,database,models
from ..controllers import emailvalidation 
from sqlalchemy.orm import Session
from passlib.hash import bcrypt
import uuid
import yagmail
from dotenv import load_dotenv
import os

load_dotenv()
EMAIL=os.getenv("EMAIL")
PASSWORD=os.getenv("PASSWORD")

get_db=database.get_db


def create_user(req:schemas.User_creation,db: Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.email==req.email).first()
    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f'User record already exist!!!')
    if len(req.mobile) == 10 and req.mobile.isnumeric() and int(req.mobile[0]) in range(6,10):
        u_id=uuid.uuid4()
        h_p= bcrypt.hash(req.password)
        h_m= bcrypt.hash(req.mobile)
        new_user=models.User(name=req.name,email=req.email,password=h_p,
                                    mobile=h_m,isVerified=False,uniqueId=str(u_id))
        if emailvalidation.validate(req.email) :
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
            yag = yagmail.SMTP(EMAIL,PASSWORD)
            contents = [
                "Thanks for signing up with us! You must follow this link to verify your account:",

               "https://fast-api-userbase.herokuapp.com/verify/"+new_user.uniqueId,

                "Have fun, and don't hesitate to contact us with your feedback."
                ]
            yag.send(new_user.email, 'Verify-Email', contents)

            return f"We have sent a verification mail to '{new_user.email}'. Please check your inbox and verify to continue."
        else:
            return '''Invalid email-id is given.Please give the correct one'''
    else: 
        return f"Please provide a valid mobile number!"




def show_all(db: Session=Depends(get_db)):
    users=db.query(models.User).all()
    return users

def show_1(id:int, db: Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} is not available")
    elif user.isVerified == False:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} is not verified")

    return user

