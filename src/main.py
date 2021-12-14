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

@app.post('/signin')
def new_user(req:models.schemas.User_creation,db: Session=Depends(get_db)):
    new_user=models.models.User(email=req.email,password=req.password,mobile=req.mobile)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

if __name__:"__main__"
uvicorn.run(app,host='127.0.0.1',port=3000)