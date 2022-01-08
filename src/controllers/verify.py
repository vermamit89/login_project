from ..models import models,database
from sqlalchemy.orm import Session
from fastapi import Depends
from dotenv import load_dotenv
import os

load_dotenv()
ADMIN_EMAIL=os.getenv("ADMIN_EMAIL")



def verify_email(uniqueId,db:Session=Depends(database.get_db)):
    user=db.query(models.User).filter(models.User.uniqueId==uniqueId).first()
    if user and user.isVerified==False:
        if user and user.email == ADMIN_EMAIL:
            user.isAdmin=1
        user.isVerified=True
        db.commit()
        db.refresh(user)
        return 'Email Verified Successfully'
    elif user and user.isVerified==True:
        return "Email Already Verified"
    else:
        return 'Email Not Verified'
    


