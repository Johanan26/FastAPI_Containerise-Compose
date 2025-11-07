from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine
from app.models import Base

app = FastAPI()

# CORS (add this block)
app.add_middleware(
CORSMiddleware,
    allow_origins=["*"], # dev-friendly; tighten in prod
    allow_methods=["*"],
    allow_headers=["*"],
)

#Replacing @app.on_event("startup")
@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield
    #Shutdown
    #Optionally close pools, flush queses, etc
    #SessionLocal.close_all()
