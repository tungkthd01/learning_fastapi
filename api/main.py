from fastapi import FastAPI, Request, Depends
from fastapi.params import Body
from pydantic import BaseModel
from api.routers import routers
import logging

app = FastAPI(title='learning Fast API', debug=True)

class Post(BaseModel):
    title: str
    content: str

@app.get('/')
async def root():
    return {'message': 'reload'}


async def logging_dependency(request: Request):
    logging.info(f'{request.method} {request.url}')
    logging.info('Params:')

    for name, value in request.path_params.items():
        logging.info(f'\t{name}: {value}')

    logging.info('Headers:')
    for name, value in request.headers.items():
        logging.info(f'\t{name}: {value}')


app.include_router(
    routers.router,
    prefix='/api-v1',
    dependencies=[
        Depends(logging_dependency),
    ]
)


import ptvsd
ptvsd.enable_attach(address=('0.0.0.0', 9001), redirect_output=True)
print('Attached!')