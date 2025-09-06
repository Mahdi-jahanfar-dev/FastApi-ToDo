from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse, Response
from fastapi.exceptions import HTTPException
from .models import User, hash_password
from db import get_db
from .schemas import UserRegisterSchema, UserLoginSchema, UserOut
from sqlalchemy.orm import Session
from users.generate_jwt_token import (
    jwt_access_token_generator,
    jwt_refresh_token_generator,
    get_access_token,
)
from fastapi_cache.decorator import cache
from typing import List


router = APIRouter(prefix="/account", tags=["account"])

# registrations route
@router.post("/register")
async def user_register(user: UserRegisterSchema, db: Session = Depends(get_db)):
    user_data = user.model_dump(exclude={"password"})
    new_user = User(**user_data)
    new_user.hashed_password = hash_password(user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return JSONResponse(
        content={"message": f"user: {new_user.username} registered"},
        status_code=status.HTTP_201_CREATED,
    )


# if we have async def or Jsonresponse cache not work
@router.get("/users/list", response_model=List[UserOut])
@cache(expire=120)
def users_list(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


# login route
@router.post("/login/")
async def user_login(user: UserLoginSchema, db: Session = Depends(get_db)):

    user_instance = db.query(User).filter_by(username=user.username).first()
    if not user_instance or not user_instance.verify_password(user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="username or password is wrong",
        )

    access_token = jwt_access_token_generator(user_instance.id)
    refresh_token = jwt_refresh_token_generator(user_instance.id)

    return JSONResponse(
        content={"access token": access_token, "refresh_token": refresh_token},
        status_code=status.HTTP_200_OK,
    )


# getting access token with refresh token route
@router.post("/token/refresh")
async def refresh_token_route(access_token: str = Depends(get_access_token)):

    return JSONResponse(
        content={"access token": access_token}, status_code=status.HTTP_201_CREATED
    )
