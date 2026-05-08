from pydantic import BaseModel


class UserSchema(BaseModel):
    username: str
    password: str
    email: str

    model_config = {"from_attributes": True}


class UserResponseSchema(BaseModel):
    id: int
    username: str
    email: str

    model_config = {"from_attributes": True}



