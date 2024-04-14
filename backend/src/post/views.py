from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.database.engine import get_db
from src.post.repositories.post_repository import post_repository
from src.post.schemas.endpoint_schema import (
    PostCreatePayload,
    PostRead,
    PostUpdatePayload,
)
from src.post.services.post_service import PostService

post_router = APIRouter()
post_service = PostService(post_repository)


@post_router.get("/")
def get_posts(db: Session = Depends(get_db)) -> list[PostRead]:
    return post_service.list_posts(db)


@post_router.post("/", status_code=status.HTTP_201_CREATED)
def create_post(post_in: PostCreatePayload, db: Session = Depends(get_db)) -> None:
    return post_service.create_post(db, post_in)


@post_router.get("/{post_id}")
def get_post(post_id: UUID, db: Session = Depends(get_db)) -> PostRead:
    return post_service.get_post(db, post_id)


@post_router.put("/{post_id}", status_code=status.HTTP_200_OK)
def update_post(post_id: UUID, post_in: PostUpdatePayload, db: Session = Depends(get_db)) -> None:
    return post_service.update_post(db, post_id, post_in)
