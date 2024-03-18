from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.database.engine import get_db
from src.profile.model import Profile
from src.profile.schemas import ProfileCreate, ProfileRead, ProfileUpdate

profile_router = APIRouter()


@profile_router.post("/", status_code=status.HTTP_201_CREATED)
def create_profile(profile_in: ProfileCreate, db: Session = Depends(get_db)):
    profile = Profile(**profile_in.model_dump())
    db.add(profile)
    db.commit()


@profile_router.get("/", response_model=list[ProfileRead])
def list_profiles(db: Session = Depends(get_db)):
    return db.query(Profile).all()


@profile_router.put("/{id}", status_code=status.HTTP_200_OK)
def update_profile(profile_id: UUID, profile_in: ProfileUpdate, db: Session = Depends(get_db)):
    profile = db.query(Profile).get(profile_id)
    if not profile:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Profile not found")

    for key, value in profile_in.model_dump().items():
        setattr(profile, key, value)

    db.commit()


@profile_router.get("/{id}", response_model=ProfileRead)
def get_profile(profile_id: UUID, db: Session = Depends(get_db)):
    profile = db.get(Profile, profile_id)
    if not profile:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Profile not found")
    return profile
