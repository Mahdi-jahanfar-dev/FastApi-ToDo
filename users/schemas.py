from pydantic import BaseModel


class UserRegisterSchema(BaseModel):
    username: str
    first_name: str
    last_name: str
    password: str


class UserLoginSchema(BaseModel):
    username: str
    password: str


class RefreshTokenSchema(BaseModel):
    refresh_token: str


class UserOut(BaseModel):
    username: str
    first_name: str
    last_name: str
    
    class Config:
        orm_mode = True