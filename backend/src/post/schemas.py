from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class PostRead(BaseModel):
    id: UUID
    content: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    scope: str
    status: str

    class Config:
        from_attributes = True


class PostCreate(BaseModel):
    content: str = Field(..., max_length=300)


class PostUpdate(BaseModel):
    content: str = Field(..., max_length=300)
