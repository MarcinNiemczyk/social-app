from typing import Optional, Type
from uuid import UUID

from sqlalchemy.orm import Session

from src.profile.interfaces.repository import IProfileRepository
from src.profile.model import Profile
from src.profile.schemas.model_schema import ProfileCreate, ProfileUpdate


class ProfileRepository(IProfileRepository):
    def create(self, db: Session, profile_in: ProfileCreate) -> None:
        profile = Profile(**profile_in.model_dump())
        db.add(profile)
        db.commit()

    def get_all(self, db: Session) -> list[Type[Profile]]:
        return db.query(Profile).all()

    def update(self, db: Session, profile_in: ProfileUpdate, profile: Profile) -> None:
        for key, value in profile_in.model_dump().items():
            setattr(profile, key, value)
        db.commit()

    def get_by_id(self, db: Session, profile_id: UUID) -> Optional[Profile]:
        return db.query(Profile).get(profile_id)
