from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.orm import Session

from ..db import models
from ..db.session import get_db
from ..schemas import user as user_schema
from ..schemas import auth as auth_schema
from ..core.security import verify_password, get_password_hash, create_access_token, decode_token

router = APIRouter(prefix="/auth", tags=["auth"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> models.User:
    payload = decode_token(token)
    if not payload or "sub" not in payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas")
    user = db.query(models.User).filter(models.User.email == payload["sub"]).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return user


@router.post("/register", response_model=user_schema.UserRead)
def register(user_in: user_schema.UserCreate, db: Session = Depends(get_db)):
    if db.query(models.User).filter(models.User.email == user_in.email).first():
        raise HTTPException(status_code=400, detail="Email já registrado")
    user = models.User(email=user_in.email, password_hash=get_password_hash(user_in.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.post("/login", response_model=auth_schema.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=400, detail="Usuário ou senha incorretos")
    access_token = create_access_token({"sub": user.email}, timedelta(minutes=30))
    return auth_schema.Token(access_token=access_token)


@router.get("/me", response_model=user_schema.UserRead)
def me(current_user: models.User = Depends(get_current_user)):
    return current_user


@router.get("/google")
def google_oauth_stub():
    return {"message": "Google OAuth ainda não implementado"}
