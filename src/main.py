from fastapi import FastAPI
from .models import models,database
from .routes import user,common,authentication,verify

app=FastAPI()

models.base.metadata.create_all(database.engine)

# app.include_router(common.router)
app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(verify.router)



# if __name__:"__main__"
# uvicorn.run(app,host='127.0.0.1',port=3000)