from fastapi import APIRouter,Depends,HTTPException,status
import models.schemas,models.database,models.models
from sqlalchemy.orm import Session
from passlib.hash import bcrypt
import models.JWToken 



router=APIRouter(tags=['Authentication'])


@router.post('/login')
def login(request:models.schemas.Login,db:Session=Depends(models.database.get_db)):
    user=db.query(models.models.User).filter(models.models.User.email==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f'wrong username')
    if not bcrypt.verify(request.password,user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f'wrong password')

   
    access_token = models.JWToken.create_access_token(data={"sub": user.email})
    return {"access_token": user, "token_type": "bearer"}