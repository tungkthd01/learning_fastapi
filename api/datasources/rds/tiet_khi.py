from typing import Any, Generic, Optional, Type, TypeVar, Union

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session
from api.models.user import TietKhi
from api.database import Base


class CRUDTietKhi():
    def __init__(self, model: Type[TietKhi]):
        self.model = model

    def create_tiet_khi(self, db: Session, tiet_khis):
        list_tiet_khi = []
        for tiet_khi in tiet_khis:
            obj_tiet_khi = self.model(**tiet_khi)
            list_tiet_khi.append(obj_tiet_khi)
            
        db.bulk_save_objects(
            list_tiet_khi,
            return_defaults=True
        )
        db.commit()
        
        
        
crud_tiet_khi = CRUDTietKhi(TietKhi)