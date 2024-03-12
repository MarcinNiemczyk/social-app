from abc import ABC, abstractmethod

from sqlalchemy.orm import Session

from src.auth.model import User
from src.auth.schemas.model_schema import UserCreate


class IAuthRepository(ABC):
    @abstractmethod
    def create(self, db: Session, user: UserCreate) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_by_email(self, db: Session, email: str) -> User:
        raise NotImplementedError
