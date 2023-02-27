from typing import Any, Generic, Optional, Type, TypeVar, Union
from fastapi import HTTPException, status

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session
from api.models.user import User
from api.database import Base


class CRUDUser():
    def __init__(self, model: Type[User]):
        self.model = model

    def create_user(self, db: Session, user):
        obj_user = self.model(**user.dict())
        db.add(obj_user)
        db.commit()
        db.refresh(obj_user)
        return  obj_user      
        
    def get_user(self, db: Session, email):
        obj_user = db.query(self.model).filter(
            self.model.email == email,
        ).first()
        if not obj_user:
            raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
        return obj_user
    
crud_use = CRUDUser(User)