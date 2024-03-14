from abc import ABC, abstractmethod
from typing import Optional, TypeVar
from uuid import UUID

from sqlalchemy.orm import Session

from src.profile.model import Profile
from src.profile.schemas import ProfileCreate, ProfileUpdate

ProfileType = TypeVar("ProfileType", bound=Profile)


class IProfileRepository(ABC):
    @abstractmethod
    def create(self, db: Session, profile_in: ProfileCreate) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_all(self, db: Session) -> list[ProfileType]:
        raise NotImplementedError

    @abstractmethod
    def update(self, db: Session, profile_in: ProfileUpdate) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, db: Session, profile_id: UUID) -> Optional[ProfileType]:
        raise NotImplementedError
