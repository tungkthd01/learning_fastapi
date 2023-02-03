from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str

@app.get('/')
async def root():
    return {'message': 'reload'}

@app.post('/createpost')
def create_post(new_post: Post):
    print("payload", new_post)
    return {'message': new_post}