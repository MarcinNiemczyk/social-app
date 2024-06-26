from typing import Optional
from uuid import UUID

from sqlalchemy.orm import Session

from src.auth.interfaces.repository import IAuthRepository
from src.auth.model import User
from src.auth.schemas.model_schema import UserCreate


class AuthRepository(IAuthRepository):
    def create(self, db: Session, user_in: UserCreate) -> None:
        user = User(**user_in.model_dump())
        db.add(user)
        db.commit()

    def get_by_email(self, db: Session, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).one_or_none()

    def get_by_id(self, db: Session, user_id: UUID) -> Optional[User]:
        return db.query(User).get(user_id)


auth_repository = AuthRepository()
