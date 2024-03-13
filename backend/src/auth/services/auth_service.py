from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from src.auth.interfaces.repository import IAuthRepository
from src.auth.schemas.endpoint_schema import UserLogin, UserRegister
from src.auth.schemas.model_schema import UserCreate
from src.auth.utils import check_password, hash_password


class AuthService:
    def __init__(self, repository: IAuthRepository):
        self.repository = repository

    def register(self, db: Session, user_in: UserRegister) -> None:
        user = self.repository.get_by_email(db, user_in.email)
        if user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail="Email already exists"
            )

        hashed_password = hash_password(user_in.password)
        self.repository.create(db, UserCreate(email=user_in.email, password=hashed_password))

    def login(self, db: Session, user_in: UserLogin) -> None:
        user = self.repository.get_by_email(db, user_in.email)
        if not user or not check_password(user_in.password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
            )
