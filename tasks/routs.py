from fastapi import APIRouter
from fastapi import Depends
from db import get_db
from .models import Task
from sqlalchemy.orm import Session


router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("/")
async def read_root(db: Session = Depends(get_db)):
    return db.query(Task).all()