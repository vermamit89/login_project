from fastapi import FastAPI
import uvicorn
import models.models,models.database,routes.user,routes.common,routes.authentication

app=FastAPI()

models.models.base.metadata.create_all(models.database.engine)

app.include_router(routes.common.router)
app.include_router(routes.authentication.router)
app.include_router(routes.user.router)


if __name__:"__main__"
uvicorn.run(app,host='127.0.0.1',port=3000)