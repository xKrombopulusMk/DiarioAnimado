from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserRead(BaseModel):
    id: int
    email: EmailStr
    plan: str
    created_at: datetime

    class Config:
        from_attributes = True
