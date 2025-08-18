from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from db import get_db
from .models import Task
from sqlalchemy.orm import Session
from .schemas import TaskCreateSchema
from users.generate_jwt_token import get_authenticated_user


router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("/")
async def read_root(db: Session = Depends(get_db), user_id: int = Depends(get_authenticated_user)):
    return db.query(Task).all()

@router.post("/create/")
async def task_create(task: TaskCreateSchema, db: Session = Depends(get_db), user_id: int = Depends(get_authenticated_user)):
    new_task = Task(title = task.title, user_id = user_id)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return JSONResponse(content={"message": f"task: {new_task.title} created"}, status_code=status.HTTP_201_CREATED)