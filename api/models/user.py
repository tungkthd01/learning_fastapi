
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from api.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))
    is_active = Column(Boolean, default=True)

    
class TietKhi(Base):
    __tablename__ = 'tiet_khi'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    tiet_khi = Column(String(255))
    start_time = Column(DateTime)
    end_time = Column(DateTime, nullable=True)
    year = Column(String(255))
    gio_soc = Column(DateTime, nullable=True)
    