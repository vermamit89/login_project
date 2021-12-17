from fastapi import FastAPI
import uvicorn
import src.models.models,src.models.database,src.routes.user,src.routes.common,src.routes.authentication,src.routes.verify

app=FastAPI()

src.models.models.base.metadata.create_all(src.models.database.engine)

app.include_router(src.routes.common.router)
app.include_router(src.routes.authentication.router)
app.include_router(src.routes.user.router)
app.include_router(src.routes.verify.router)



if __name__:"__main__"
uvicorn.run(app,host='127.0.0.1',port=3000)