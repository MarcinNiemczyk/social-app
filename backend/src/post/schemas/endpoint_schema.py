from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from src.core.base_schema import CustomBaseModel


class PostRead(CustomBaseModel):
    id: UUID
    content: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    scope: str
    status: str

    class Config:
        from_attributes = True


class PostCreatePayload(CustomBaseModel):
    content: str = Field(..., max_length=300)


class PostUpdatePayload(CustomBaseModel):
    content: str = Field(..., max_length=300)
