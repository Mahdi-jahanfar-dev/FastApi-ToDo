from pydantic import BaseModel


class UserRegisterSchema(BaseModel):
    username: str
    first_name: str
    last_name: str
    password: str
    
    
class UserLoginSchema(BaseModel):
    username: str
    password: str