from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship, backref
from db import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(ForeignKey("users.id"))
    title = Column(
        String(length=100),
    )
    created_at = Column(DateTime, default=func.now())
    user = relationship("User", back_populates="tasks")