from typing import Optional

from pydantic import BaseModel, Field


class ProfileCreate(BaseModel):
    display_name: str = Field(..., max_length=255)
    name: Optional[str] = Field(None, max_length=70)
    surname: Optional[str] = Field(None, max_length=70)


class ProfileUpdate(BaseModel):
    display_name: str = Field(..., max_length=255)
    name: Optional[str] = Field(None, max_length=70)
    surname: Optional[str] = Field(None, max_length=70)
