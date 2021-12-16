from fastapi import FastAPI
import uvicorn
import models.models,models.database,routes.user

app=FastAPI()

models.models.base.metadata.create_all(models.database.engine)

app.include_router(routes.user.router)



@app.get('/')
def start():
    return "server is live"

if __name__:"__main__"
uvicorn.run(app,host='127.0.0.1',port=3000)