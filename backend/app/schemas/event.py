from datetime import datetime
from pydantic import BaseModel
from typing import Any


class EventCreate(BaseModel):
    type: str
    content: Any


class EventRead(BaseModel):
    id: int
    type: str
    content: Any
    created_at: datetime

    class Config:
        from_attributes = True
