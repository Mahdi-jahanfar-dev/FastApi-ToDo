from fastapi import FastAPI
from config import settings
from db import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from tasks.models import Task  # Assuming you have a Task model defined in tasks.py

app = FastAPI()


@app.get("/")
async def read_root(db: Session = Depends(get_db)):
    return db.query(Task).all()