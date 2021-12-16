from fastapi import APIRouter,Depends,HTTPException,status
import models.schemas,models.database,models.models
from sqlalchemy.orm import Session
from passlib.hash import bcrypt



router=APIRouter(tags=['Authentication'])


@router.post('/login')
def login(request:models.schemas.Login,db:Session=Depends(models.database.get_db)):
    user=db.query(models.models.User).filter(models.models.User.email==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f'Invalid Credentials')
    if not bcrypt.verify('request.password',bcrypt.hash("req.password")):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f'wrong password')

    return user