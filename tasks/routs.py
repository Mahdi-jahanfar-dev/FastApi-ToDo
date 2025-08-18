from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from db import get_db
from .models import Task
from sqlalchemy.orm import Session
from .schemas import TaskCreateSchema


router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("/")
async def read_root(db: Session = Depends(get_db)):
    return db.query(Task).all()

@router.post("/create/")
async def task_create(task: TaskCreateSchema, db: Session = Depends(get_db)):
    new_task = Task(title = task.title)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return JSONResponse(content={"message": f"task: {new_task.title} created"}, status_code=status.HTTP_201_CREATED)