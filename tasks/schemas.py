from pydantic import BaseModel


class TaskCreateSchema(BaseModel):
    title: str
