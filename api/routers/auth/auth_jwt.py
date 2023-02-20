from datetime import datetime, timedelta

from fastapi import Depends, FastAPI, HTTPException, status, APIRouter, Body
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from sqlalchemy.orm import Session
from api.database import get_db
from api.datasources.rds.user import crud_use

router = APIRouter()

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    email: str | None = None
    

class User(BaseModel):
    email: str | None = None
    is_active: bool | None = None
    
class UserInfor(BaseModel):
    email:  str 
    hashed_password: str


class UserInDB(User):
    hashed_password: str
    

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

    

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(session: Session= Depends(get_db),token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception
    user = crud_use.get_user(db=session, email=token_data.email)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


def hash_password(password):
    return pwd_context.hash(password)


@router.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return {"email":current_user.email}


@router.get("/users/me/items/")
async def read_own_items(current_user: User = Depends(get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.email}]

    

@router.post('/user', response_model=User)
def create_user(
    session: Session = Depends(get_db),
    user: UserInfor = Body()
):
    user.hashed_password = hash_password(user.hashed_password)
    new_user = crud_use.create_user(db=session, user=user)
    return User(
        email=new_user.email,
        is_active=new_user.is_active
    )
    
@router.post('/login', response_model=Token)
def log_in(
    session: Session = Depends(get_db),
    user: UserInfor = Body()
):
    obj_user = crud_use.get_user(db=session,email=user.email)
    verify_pass = verify_password(user.hashed_password, obj_user.hashed_password)
    if not verify_pass:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    access_token = create_access_token(
        data={"sub": obj_user.email,
              "is_active": obj_user.id}, expires_delta=access_token_expires
    )
    return Token(
        access_token=access_token,
        token_type = "bearer"
    )