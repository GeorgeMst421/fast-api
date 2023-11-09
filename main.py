from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas, crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    

@app.post("/users", response_model=schemas.User)

def create_user(user: schemas.UserCreate, db:Session = Depends(get_db)):
    pass


