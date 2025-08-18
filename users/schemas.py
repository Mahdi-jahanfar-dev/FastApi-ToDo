from pydantic import BaseModel


class UserRegisterSchema(BaseModel):
    username: str
    first_name: str
    last_name: str
    password: str