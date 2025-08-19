import time
from pathlib import Path
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..db import models
from ..db.session import get_db
from ..schemas import episode as episode_schema
from .auth import get_current_user
from ..services.nlp import summarizer, narrator
from ..services.tts import tts_service
from ..services.cartoon import cartoon_service

router = APIRouter(prefix="/episodes", tags=["episodes"])


@router.post("/create", response_model=episode_schema.EpisodeRead)
def create_episode(ep_in: episode_schema.EpisodeCreate, db: Session = Depends(get_db), user: models.User = Depends(get_current_user)):
    events = db.query(models.Event).filter(models.Event.user_id == user.id).all()
    bullets = summarizer.summarize_events([{"content": e.content} for e in events])
    tone = ep_in.style if ep_in.style in ["poetic", "funny", "minimal"] else "minimal"
    text = narrator.narrate(bullets, style=tone)
    episode = models.Episode(user_id=user.id, period=ep_in.period, style=ep_in.style, text=text, status="done")
    timestamp = int(time.time())
    if ep_in.style == "audio":
        audio_path = f"storage/episodes/ep_{user.id}_{timestamp}.mp3"
        tts_service.synthesize(text, audio_path)
        episode.audio_path = audio_path
    if ep_in.style == "cartoon":
        video_path = f"storage/episodes/ep_{user.id}_{timestamp}.mp4"
        cartoon_service.create_cartoon(bullets, video_path)
        episode.video_path = video_path
    db.add(episode)
    db.commit()
    db.refresh(episode)
    return episode


@router.get("/{episode_id}", response_model=episode_schema.EpisodeRead)
def get_episode(episode_id: int, db: Session = Depends(get_db), user: models.User = Depends(get_current_user)):
    episode = db.query(models.Episode).filter(models.Episode.id == episode_id, models.Episode.user_id == user.id).first()
    if not episode:
        raise HTTPException(status_code=404, detail="Episódio não encontrado")
    return episode


@router.get("/share/{episode_id}")
def share_episode(episode_id: int, db: Session = Depends(get_db), user: models.User = Depends(get_current_user)):
    episode = db.query(models.Episode).filter(models.Episode.id == episode_id, models.Episode.user_id == user.id).first()
    if not episode:
        raise HTTPException(status_code=404, detail="Episódio não encontrado")
    return {"text": episode.text, "audio": episode.audio_path, "video": episode.video_path}
