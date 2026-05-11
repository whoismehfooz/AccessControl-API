from pydantic import BaseModel
from typing import List







class TokenResponseSchema(BaseModel):
    access_token: str
    token_type: str

    class Config:
        from_attributes = True



class LoginSchema(BaseModel):
    username: str
    password: str

    class Config:
        from_attributes = True