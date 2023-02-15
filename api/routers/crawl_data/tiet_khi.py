from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.database import get_db
from api.datasources.rds.tiet_khi import crud_tiet_khi
from api.service.crawl_data_website import craw_tiet_khi
from pydantic import BaseModel

router = APIRouter()


@router.get('/crawl_data_tiet_khi/', response_model=None)
def crawl(
    session: Session = Depends(get_db)
):
    data = craw_tiet_khi()
    # data = [{'gio_soc': None, 'year': '1800', 'start_time': '1800-01-05 18:37:00', 'tiet_khi': 'Tiểu hàn', 'end_time': '1800-01-20 12:07:00'}]
    crud_tiet_khi.create_tiet_khi(db=session, tiet_khis=data)
    return {'message': 'success'}