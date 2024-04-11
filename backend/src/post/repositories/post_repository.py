from typing import Type
from uuid import UUID

from sqlalchemy.orm import Session

from src.post.interfaces.repository import IPostRepository
from src.post.model import Post
from src.post.schemas.model_schema import PostCreate, PostUpdate


class PostRepository(IPostRepository):
    def create(self, db: Session, post_in: PostCreate) -> None:
        post = Post(**post_in.model_dump())
        db.add(post)
        db.commit()

    def get_all(self, db: Session) -> list[Type[Post]]:
        return db.query(Post).all()

    def update(self, db: Session, post_in: PostUpdate, post: Post) -> None:
        for key, value in post_in.model_dump().items():
            setattr(post, key, value)
        db.commit()

    def get_by_id(self, db: Session, post_id: UUID) -> Post | None:
        return db.query(Post).get(post_id)


post_repository = PostRepository()
