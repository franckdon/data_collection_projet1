from typing import Union
from fastapi import FastAPI, Depends

from sqlalchemy import select, create_engine
from sqlalchemy.orm import Session

import crud, models, schemas

from .database import SessionLocal, engine



hostname="127.0.0.1:8889"
dbname="dataCollection"
uname="root"
pwd="root"

models.Base.metadata.create_all(bind=engine)

app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/devises/", response_model=list[schemas.Devise])
def read_devises(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    devises = crud.get_devises(db, skip=skip, limit=limit)
    return devises