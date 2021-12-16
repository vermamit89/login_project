from typing import List
from fastapi import FastAPI,Depends,status,HTTPException
from passlib.hash import bcrypt
import uvicorn
import models.schemas,models.models,models.database
from sqlalchemy.orm import Session



app=FastAPI()

models.models.base.metadata.create_all(models.database.engine)

def get_db():
    db=models.database.sessionlocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
def start():
    return "server is live"


@app.post('/user/signin',status_code=status.HTTP_201_CREATED)
def new_user(req:models.schemas.User_creation,db: Session=Depends(get_db)):
    h_p= bcrypt.hash("req.password")
    h_m= bcrypt.hash("req.mobile")
    new_user=models.models.User(name=req.name,email=req.email,password=h_p,mobile=h_m)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get('/user',status_code=status.HTTP_200_OK,response_model=List[models.schemas.Show_User])
def show_all(db: Session=Depends(get_db)):
    users=db.query(models.models.User).all()
    return users

@app.get('/user/{id}',status_code=status.HTTP_200_OK,response_model=models.schemas.Show_User)
def show_single_user(id,db: Session=Depends(get_db)):
    user=db.query(models.models.User).filter(models.models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with id {id} is not available")

    return user



if __name__:"__main__"
uvicorn.run(app,host='127.0.0.1',port=3000)