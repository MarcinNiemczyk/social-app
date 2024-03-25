from abc import ABC, abstractmethod
from typing import Optional, TypeVar
from uuid import UUID

from sqlalchemy.orm import Session

from src.auth.model import User
from src.auth.schemas.model_schema import UserCreate

UserType = TypeVar("UserType", bound=User)


class IAuthRepository(ABC):
    @abstractmethod
    def create(self, db: Session, user_in: UserCreate) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_by_email(self, db: Session, email: str) -> Optional[UserType]:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, db: Session, user_id: UUID) -> Optional[UserType]:
        raise NotImplementedError
