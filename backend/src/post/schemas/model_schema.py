from pydantic import BaseModel, Field


class PostCreate(BaseModel):
    content: str = Field(..., max_length=300)


class PostUpdate(BaseModel):
    content: str = Field(..., max_length=300)
