from fastapi import FastAPI, HTTPException, status, Response, Depends
from fastapi.params import Body
from typing import Optional, List
from . import models, schemas, utils
from .database import engine, get_db
from sqlalchemy.orm import Session
from .routers import post, user, auth



models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get("/")
def index():
    return {"ok"}

