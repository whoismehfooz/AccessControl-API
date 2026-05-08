from fastapi import HTTPException, status
from pwdlib import PasswordHash
from sqlalchemy.orm import Session
from src.user.models import UserModel
from src.user.schemas import UserSchema


password_hasher = PasswordHash.recommended()

def get_hash_password(password):
    return password_hasher.hash(password)



def create_user(db: Session, data: UserSchema):
    existing_user = db.query(UserModel).filter(UserModel.username == data.username).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists"
        )
    
    existing_email = db.query(UserModel).filter(UserModel.email == data.email).first()
    if existing_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists"
        )
    
    hashed_password = get_hash_password(data.password)

    new_user = UserModel(
        username=data.username,
        email=data.email,
        hashed_password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user



def get_all_users(db: Session):
    return db.query(UserModel).all()