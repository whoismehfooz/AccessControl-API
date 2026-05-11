from fastapi import HTTPException, status
from src.user.schemas import UserResponseSchema
from src.user.models import UserModel
from sqlalchemy.orm import Session
from src.auth.utils import verify_password, create_access_token
from src.auth.schemas import LoginSchema








def login_user(db: Session, data: LoginSchema):
    existing_user = db.query(UserModel).filter(UserModel.username == data.username).first()
    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid username"
        )

    if not verify_password(data.password, existing_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid password"
        )
    
    token = create_access_token({"sub": str(existing_user.id), 'role': existing_user.role})

    return {
        "access_token": token,
        'token_type': 'bearer'
    }