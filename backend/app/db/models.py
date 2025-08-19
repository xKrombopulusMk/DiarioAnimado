from datetime import datetime
from enum import Enum
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, JSON, Enum as PgEnum
from sqlalchemy.orm import relationship

from .session import Base


class PlanEnum(str, Enum):
    free = "free"
    premium = "premium"


class EventType(str, Enum):
    message = "message"
    music = "music"
    photo = "photo"
    location = "location"
    note = "note"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    plan = Column(String, default=PlanEnum.free.value)
    created_at = Column(DateTime, default=datetime.utcnow)

    events = relationship("Event", back_populates="user")
    episodes = relationship("Episode", back_populates="user")


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    type = Column(PgEnum(EventType))
    content = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="events")


class Episode(Base):
    __tablename__ = "episodes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    period = Column(String)
    style = Column(String)
    text = Column(String, nullable=True)
    audio_path = Column(String, nullable=True)
    video_path = Column(String, nullable=True)
    status = Column(String, default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)
    finished_at = Column(DateTime, nullable=True)

    user = relationship("User", back_populates="episodes")


class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    plan = Column(String)
    active = Column(Boolean, default=True)
    started_at = Column(DateTime, default=datetime.utcnow)
    renewed_at = Column(DateTime, nullable=True)
