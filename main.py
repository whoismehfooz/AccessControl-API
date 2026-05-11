from fastapi import FastAPI , APIRouter
from src.utils.db import Base, engine
from src.user.models import UserModel

from src.user.routers import user_router
from src.auth.routers import auth_router








app = FastAPI(title="Access Control API", )


Base.metadata.create_all(bind=engine)
app.include_router(user_router)
app.include_router(auth_router)