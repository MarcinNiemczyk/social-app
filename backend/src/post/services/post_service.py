from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from src.post.interfaces.repository import IPostRepository
from src.post.schemas.endpoint_schema import (
    PostCreatePayload,
    PostRead,
    PostUpdatePayload,
)
from src.post.schemas.model_schema import PostCreate, PostUpdate


class PostService:
    def __init__(self, repository: IPostRepository):
        self.repository = repository

    def create_post(self, db: Session, post_in: PostCreatePayload) -> None:
        self.repository.create(db, PostCreate(**post_in.model_dump()))

    def list_posts(self, db: Session) -> list[PostRead]:
        posts = self.repository.get_all(db)
        return [PostRead.model_validate(post) for post in posts]

    def update_post(self, db: Session, post_id: UUID, post_in: PostUpdatePayload) -> None:
        post = self.repository.get_by_id(db, post_id)
        if not post:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
        self.repository.update(db, PostUpdate(**post_in.model_dump()), post)

    def get_post(self, db: Session, post_id: UUID) -> PostRead:
        post = self.repository.get_by_id(db, post_id)
        if not post:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
        return post
