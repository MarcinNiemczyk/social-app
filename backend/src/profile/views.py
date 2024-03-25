from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.auth.views import auth_repository
from src.database.engine import get_db
from src.middleware.auth import must_be_logged_in
from src.profile.repositories.profile_repository import ProfileRepository
from src.profile.schemas.endpoint_schema import (
    ProfileCreatePayload,
    ProfileUpdatePayload,
)
from src.profile.services.profile_service import ProfileService

profile_router = APIRouter()
profile_repository = ProfileRepository()
profile_service = ProfileService(profile_repository, auth_repository)


@profile_router.post("/", status_code=status.HTTP_201_CREATED, dependencies=[Depends(must_be_logged_in)])
def create_profile(profile_in: ProfileCreatePayload, db: Session = Depends(get_db)):
    return profile_service.create_profile(db, profile_in)


@profile_router.get("/")
def list_profiles(db: Session = Depends(get_db)):
    return profile_service.list_profiles(db)


@profile_router.put("/{id}", status_code=status.HTTP_200_OK, dependencies=[Depends(must_be_logged_in)])
def update_profile(profile_id: UUID, profile_in: ProfileUpdatePayload, db: Session = Depends(get_db)):
    return profile_service.update_profile(db, profile_id, profile_in)


@profile_router.get("/{id}")
def get_profile(profile_id: UUID, db: Session = Depends(get_db)):
    return profile_service.get_profile(db, profile_id)
