from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.utils.db import get_db
from src.user.schemas import UserSchema, UserResponseSchema
from src.user.controllers import create_user, get_all_users




user_router = APIRouter(prefix='/users', tags=['Users'])


@user_router.post('/', response_model=UserResponseSchema, status_code=status.HTTP_201_CREATED)
async def register_user_endpoint(data: UserSchema, db: Session = Depends(get_db)):
    return create_user(db, data)


@user_router.get('/', response_model=list[UserResponseSchema], status_code=status.HTTP_200_OK)
async def get_all_users_endpoint(db: SessiasswordSchemaon = Depends(get_db)):
    return get_all_users(db)