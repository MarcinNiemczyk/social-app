from fastapi import APIRouter, Depends, HTTPException, status
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from src.auth.model import User
from src.auth.schemas import UserLogin, UserRegister
from src.database.engine import get_db

auth_router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@auth_router.post("/register", status_code=status.HTTP_201_CREATED)
def register(user_in: UserRegister, db_session: Session = Depends(get_db)):
    user = db_session.query(User).filter(User.email == user_in.email).one_or_none()
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Email already exists"
        )

    hashed_password = pwd_context.hash(user_in.password)

    user = User(email=user_in.email, password=hashed_password)
    db_session.add(user)
    db_session.commit()


@auth_router.post("/login")
def login(user_in: UserLogin, db_session: Session = Depends(get_db)):
    user = db_session.query(User).filter(User.email == user_in.email).one_or_none()
    if not user or not pwd_context.verify(user_in.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )
    return {"status": "Logged in successfully"}