from fastapi import FastAPI
from config import settings
from db import get_db, Base, engine
from sqlalchemy.orm import Session
from fastapi import Depends
from tasks.models import Task  # Assuming you have a Task model defined in tasks.py
from tasks.routs import router as tasks_router
from users.routes import router as users_router
from contextlib import asynccontextmanager
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
import redis.asyncio as ioredis


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("application startup")
    redis = ioredis.from_url(
        "redis://redis:6379", encoding="utf8", decode_responses=True
    )
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    yield
    print("application shutdown")


app = FastAPI(title="task manager app", lifespan=lifespan)


app.include_router(tasks_router)
app.include_router(users_router)
