from fastapi import FastAPI
from config import settings
from db import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from tasks.models import Task  # Assuming you have a Task model defined in tasks.py
from tasks.routs import router as tasks_router
from users.routes import router as users_router

app = FastAPI(title="task manager app")


app.include_router(tasks_router)
app.include_router(users_router)