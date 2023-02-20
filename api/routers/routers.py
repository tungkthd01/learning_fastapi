from fastapi import APIRouter

from api.routers.crawl_data import tiet_khi
from api.routers.auth import auth_jwt

router = APIRouter()


router.include_router(
    tiet_khi.router, prefix='/tiet_khi', tags=['tiet_khi']
)

router.include_router(
    auth_jwt.router,prefix='/auth', tags=['auth']
)