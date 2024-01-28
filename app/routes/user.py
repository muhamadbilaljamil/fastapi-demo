print("User Route")
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from .. import controllers, models, schemas
from ..config.db import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

user = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@user.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = controllers.user.get_users(db, skip=skip, limit=limit)
    return users

@user.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = controllers.user.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@user.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = controllers.user.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return controllers.user.create_user(db=db, user=user)


