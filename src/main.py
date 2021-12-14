from fastapi import FastAPI,Depends


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

@app.post('/user/signin')
def new_user(req:models.schemas.User_creation,db: Session=Depends(get_db)):
    new_user=models.models.User(email=req.email,password=req.password,mobile=req.mobile)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get('/user')
def show_all(db: Session=Depends(get_db)):
    users=db.query(models.models.User).all()
    return users

@app.get('/user/{id}')
def show_single_user(id,db: Session=Depends(get_db)):
    user=db.query(models.models.User).filter(models.models.User.id==id).first()
    return user



if __name__:"__main__"
uvicorn.run(app,host='127.0.0.1',port=3000)