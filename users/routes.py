from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from .models import User, hash_password
from db import get_db
from .schemas import UserRegisterSchema
from sqlalchemy.orm import Session

router = APIRouter(prefix="/account", tags=["account"])

@router.post("/register")
async def user_register(user: UserRegisterSchema, db: Session = Depends(get_db)):
    user_data = user.model_dump(exclude={"password"})
    new_user = User(**user_data)
    new_user.hashed_password = hash_password(user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return JSONResponse(content={"message": f"user: {new_user.username} registered"})

@router.get("users/list")
async def users_list(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users