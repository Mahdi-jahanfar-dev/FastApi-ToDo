from pydantic import BaseModel


# schema for user registration
class UserRegisterSchema(BaseModel):
    username: str
    first_name: str
    last_name: str
    password: str


# schema for user login
class UserLoginSchema(BaseModel):
    username: str
    password: str


# schema for getting access token with refresh token
class RefreshTokenSchema(BaseModel):
    refresh_token: str


# schema for user informations
class UserOut(BaseModel):
    username: str
    first_name: str
    last_name: str
    
    class Config:
        orm_mode = True