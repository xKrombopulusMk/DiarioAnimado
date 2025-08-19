from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..db import models
from ..db.session import get_db
from ..schemas import event as event_schema
from .auth import get_current_user

router = APIRouter(prefix="/data", tags=["data"])


@router.post("/upload", response_model=event_schema.EventRead)
def upload(event_in: event_schema.EventCreate, db: Session = Depends(get_db), user: models.User = Depends(get_current_user)):
    event = models.Event(user_id=user.id, type=event_in.type, content=event_in.content)
    db.add(event)
    db.commit()
    db.refresh(event)
    return event


@router.post("/import")
def import_stub():
    return {"message": "Integrações ainda não implementadas"}
