from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Optional, TypeVar

from sqlalchemy.orm import Session

from src.auth.schemas.model_schema import UserCreate

if TYPE_CHECKING:
    from src.auth.model import User

    UserType = TypeVar("UserType", bound=User)


class IAuthRepository(ABC):
    @abstractmethod
    def create(self, db: Session, user_in: UserCreate) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_by_email(self, db: Session, email: str) -> Optional[UserType]:
        raise NotImplementedError
