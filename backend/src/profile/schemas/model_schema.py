from typing import Optional
from uuid import UUID

from pydantic import Field

from src.core.base_schema import CustomBaseModel


class ProfileCreate(CustomBaseModel):
    display_name: str = Field(..., max_length=255)
    user_id: UUID
    name: Optional[str] = Field(None, max_length=70)
    surname: Optional[str] = Field(None, max_length=70)


class ProfileUpdate(CustomBaseModel):
    display_name: str = Field(..., max_length=255)
    name: Optional[str] = Field(None, max_length=70)
    surname: Optional[str] = Field(None, max_length=70)
