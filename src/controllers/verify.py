from ..models import models,database
from sqlalchemy.orm import Session
from fastapi import Depends



def verify_email(uniqueId,db:Session=Depends(database.get_db)):
    # U_ID=db.query(models.models.User).filter(models.models.User.uniqueId==uniqueId).first()
    user=db.query(models.User).filter(models.User.uniqueId==uniqueId).first()
    # IV=db.query(models.models.User).filter(models.models.User.isVerified).first()
    if user and user.isVerified==False:
        user.isVerified=True
        # user.isVerified(True)
        db.commit()
        db.refresh(user)
        return 'Email Verified Successfully'
    elif user and user.isVerified==True:
        return "Email Already Verified"
    else:
        return 'Email Not Verified'