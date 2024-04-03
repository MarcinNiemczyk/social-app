from abc import ABC, abstractmethod
from typing import Optional, TypeVar
from uuid import UUID

from sqlalchemy.orm import Session

from src.post.model import Post
from src.post.schemas.model_schema import PostCreate, PostUpdate

PostType = TypeVar("PostType", bound=Post)


class IPostRepository(ABC):
    @abstractmethod
    def create(self, db: Session, post_in: PostCreate) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_all(self, db: Session) -> list[PostType]:
        raise NotImplementedError

    @abstractmethod
    def update(self, db: Session, post_in: PostUpdate, post: PostType) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, db: Session, post_id: UUID) -> Optional[PostType]:
        raise NotImplementedError
