import models.models,models.database
from sqlalchemy.orm import Session
from fastapi import Depends



def verify_email(uniqueId,db:Session=Depends(models.database.get_db)):
    # U_ID=db.query(models.models.User).filter(models.models.User.uniqueId==uniqueId).first()
    user=db.query(models.models.User).filter(models.models.User.uniqueId==uniqueId).first()
    # IV=db.query(models.models.User).filter(models.models.User.isVerified).first()
    if user and user.isVerified==False:
        user.isVerified=True
        # user.isVerified(True)
        db.commit()
        db.refresh(user)
        return 'Verified Successfully'
    elif user and user.isVerified==True:
        return "Already Verified"
    else:
        return 'Not Verified'