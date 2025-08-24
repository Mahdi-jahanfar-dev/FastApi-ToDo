from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from db import get_db
from .models import Task
from sqlalchemy.orm import Session
from .schemas import TaskCreateSchema
from users.generate_jwt_token import get_authenticated_user


router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("/")
async def read_root(
    db: Session = Depends(get_db), user_id: int = Depends(get_authenticated_user)
):
    return db.query(Task).filter_by(user_id=user_id).all()


@router.post("/create/")
async def task_create(
    task: TaskCreateSchema,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_authenticated_user),
):
    new_task = Task(title=task.title, user_id=user_id)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return JSONResponse(
        content={"message": f"task: {new_task.title} created"},
        status_code=status.HTTP_201_CREATED,
    )


@router.put("/{task_id}")
async def task_update(
    task_id: int,
    task: TaskCreateSchema,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_authenticated_user),
):
    current_task = db.query(Task).filter_by(id=task_id, user_id=user_id).first()
    if not current_task:
        raise HTTPException(
            detail="task not found", status_code=status.HTTP_400_BAD_REQUEST
        )
    current_task.title = task.title
    db.commit()
    db.refresh(current_task)
    return JSONResponse(
        content={"message": "successfully edited"}, status_code=status.HTTP_200_OK
    )


@router.delete("/del/{task_id}")
async def task_delete(
    task_id: int,
    user_id: int = Depends(get_authenticated_user),
    db: Session = Depends(get_db),
):

    task = db.query(Task).filter_by(id=task_id, user_id=user_id).first()
    if not task:
        raise HTTPException(
            detail="task not found", status_code=status.HTTP_400_BAD_REQUEST
        )
    db.delete(task)
    db.commit()
    return JSONResponse(
        content={"message": "task deleted successfully"}, status_code=status.HTTP_200_OK
    )
