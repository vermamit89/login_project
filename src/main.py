from fastapi import FastAPI
import uvicorn

app=FastAPI()

@app.get('/')
def start():
    return "server is live"

@app.post('/signin')
def new_user(req:schemas.User_creation):
    return {'data':f'sign-in completed with email as {req.email}'}

if __name__:"__main__"
uvicorn.run(app,host='127.0.0.1',port=3000)