from uuid import UUID

from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.auth.interfaces.repository import IAuthRepository
from src.profile.interfaces.repository import IProfileRepository
from src.profile.schemas.endpoint_schema import (
    ProfileCreatePayload,
    ProfileRead,
    ProfileUpdatePayload,
)
from src.profile.schemas.model_schema import ProfileCreate, ProfileUpdate


class ProfileService:
    def __init__(self, repository: IProfileRepository, auth_repository: IAuthRepository):
        self.repository = repository
        self.auth_repository = auth_repository

    def create_profile(self, db: Session, profile_in: ProfileCreatePayload, user_id: UUID) -> None:
        user = self.auth_repository.get_by_id(db, user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        self.repository.create(db, ProfileCreate(**profile_in.model_dump(), user_id=user_id))

    def list_profiles(self, db: Session) -> list[ProfileRead]:
        profiles = self.repository.get_all(db)
        return [ProfileRead.model_validate(profile) for profile in profiles]

    def update_profile(self, db: Session, profile_id: UUID, profile_in: ProfileUpdatePayload) -> None:
        profile = self.repository.get_by_id(db, profile_id)
        self.repository.update(db, ProfileUpdate(**profile_in.model_dump()), profile)

    def get_profile(self, db: Session, profile_id: UUID) -> ProfileRead:
        profile = self.repository.get_by_id(db, profile_id)
        return ProfileRead.model_validate(profile)
