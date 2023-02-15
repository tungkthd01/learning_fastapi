from fastapi import APIRouter

from api.routers.crawl_data import tiet_khi

router = APIRouter()


router.include_router(
    tiet_khi.router, prefix='/tiet_khi', tags=['tiet_khi']
)