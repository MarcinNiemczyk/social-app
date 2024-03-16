from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.auth.repositories.auth_repository import AuthRepository
from src.auth.schemas.endpoint_schema import TokenResponse, UserLogin, UserRegister
from src.auth.services.auth_service import AuthService
from src.database.engine import get_db

auth_router = APIRouter()
auth_repository = AuthRepository()
auth_service = AuthService(repository=auth_repository)


@auth_router.post("/register", status_code=status.HTTP_201_CREATED)
def register(user_in: UserRegister, db_session: Session = Depends(get_db)) -> None:
    auth_service.register(db_session, user_in)


@auth_router.post("/login")
def login(user_in: UserLogin, db_session: Session = Depends(get_db)) -> TokenResponse:
    auth_service.login(db_session, user_in)
    return auth_service.login(db_session, user_in)