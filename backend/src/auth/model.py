from uuid import UUID, uuid4

from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.engine import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[bytes]
    profiles = relationship("Profile", back_populates='user')
