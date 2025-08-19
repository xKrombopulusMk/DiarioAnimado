from fastapi import FastAPI
from .api import auth, data, episodes, admin
from .db.session import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Diário Animado")

app.include_router(auth.router)
app.include_router(data.router)
app.include_router(episodes.router)
app.include_router(admin.router)
