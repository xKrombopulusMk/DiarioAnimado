from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class EpisodeCreate(BaseModel):
    period: str
    style: str


class EpisodeRead(BaseModel):
    id: int
    period: str
    style: str
    text: Optional[str] = None
    audio_path: Optional[str] = None
    video_path: Optional[str] = None
    status: str
    created_at: datetime
    finished_at: Optional[datetime] = None

    class Config:
        from_attributes = True
