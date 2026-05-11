from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.utils.db import get_db
from src.auth.controllers import login_user
from src.auth.utils import get_current_user, admin_only
from src.auth.schemas import TokenResponseSchema, LoginSchema
from src.user.models import UserModel



auth_router = APIRouter(prefix='/auth', tags=['Authentication'])


@auth_router.post('/login', response_model=TokenResponseSchema, status_code=200)
async def login_user_endpoint(data: LoginSchema, db: Session = Depends(get_db)):
    return login_user(db, data)


@auth_router.get('/me', status_code=200)
async def get_current_user_endpoint(current_user: UserModel = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email,
        "role": current_user.role
    }

@auth_router.get('/admin', status_code=200)
async def admin_only_endpoint(current_user: UserModel = Depends(admin_only)):
    return {
        "message": f'Welcome, Admin {current_user.username}!'
    }