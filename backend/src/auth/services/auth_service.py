from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from src.auth.interfaces.repository import IAuthRepository
from src.auth.schemas.endpoint_schema import TokenResponse, UserLogin, UserRegister
from src.auth.schemas.model_schema import UserCreate
from src.auth.utils import (
    check_password,
    get_access_token,
    get_refresh_token,
    hash_password,
)


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

    def login(self, db: Session, user_in: UserLogin) -> TokenResponse:
        user = self.repository.get_by_email(db, user_in.email)
        if not user or not check_password(user_in.password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
            )
        return AuthService.generate_tokens_response(user.id)

    @staticmethod
    def generate_tokens_response(user_id: UUID) -> TokenResponse:
        access_token = get_access_token({
            "sub": str(user_id),
        })
        refresh_token = get_refresh_token({
            "sub": str(user_id),
        })
        token_type = "bearer"
        return TokenResponse(access_token=access_token, refresh_token=refresh_token, token_type=token_type)
