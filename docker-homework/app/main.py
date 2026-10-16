import uvicorn
from fastapi import Depends, FastAPI
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import get_db

from typing import Literal

#TaskStatus = Literal["open", "in_progress", "done"]
#TaskPriority = Literal["low", "medium", "high"]

app = FastAPI(title="fastAPI attempt")

@app.get('/')
def hello():
    return {"message" : "test"}

@app.get('/health')
def health() -> dict[str, str]:
    return {"status" : "ok"}

@app.get('/{project_id}')
def health() -> dict[str, str]:
    return {"status" : "ok"}

if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0")