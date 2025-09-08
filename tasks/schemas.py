from pydantic import BaseModel


# schema for creating task
class TaskCreateSchema(BaseModel):
    title: str


class OpenAiMessageSchema(BaseModel):
    message: str