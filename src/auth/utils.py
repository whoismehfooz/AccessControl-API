import jwt
from jwt import InvalidTokenError
from datetime import datetime, timedelta
from fastapi import HTTPException, status
from pwdlib import PasswordHash
from src.utils.settings import settings
from sqlalchemy.orm import Session
from src.utils.db import get_db
from src.user.models import UserModel
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer






oauth2scheme = OAuth2PasswordBearer(tokenUrl='/auth/login')
password_hasher = PasswordHash.recommended()

def verify_password(plain_password, hashed_password):
    return password_hasher.verify(plain_password, hashed_password)


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    return encoded_jwt


def decode_access_token(token:str, db: Session):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])

        user_id = int(payload.get('sub')) 
        user_role = payload.get('role')

        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token"
            )
        existing_user = db.query(UserModel).filter(UserModel.id == user_id).first()

        if not existing_user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found"
            )
        return existing_user

    except InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )
        

def get_current_user(token: str = Depends(oauth2scheme), db: Session = Depends(get_db)):
    return decode_access_token(token, db)


def admin_only(current_user: UserModel = Depends(get_current_user)):
    if current_user.role != 'admin':
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Admin privileges required'
        )

    return current_user