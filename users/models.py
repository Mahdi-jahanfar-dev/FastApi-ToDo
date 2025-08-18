from db import Base
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship, backref
from passlib.context import CryptContext  # برای هش و بررسی رمز عبور


pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")

def hash_password(plain_password: str) -> str:
    return pwd_context.hash(plain_password)

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(length=50))
    first_name = Column(String(length=100))
    last_name = Column(String(length=200))
    hashed_password = Column(String(200))
    created_at = Column(DateTime,)
    
    def verify(plain_password: str, hashed_password: str = hashed_password) -> bool:
        return pwd_context.verify(plain_password, hashed_password)
    
    def __repr__(self):
        return self.username