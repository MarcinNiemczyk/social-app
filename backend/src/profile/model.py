from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from sqlalchemy import ForeignKey, types
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.engine import Base


class Profile(Base):
    __tablename__ = "profiles"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    display_name: Mapped[str] = mapped_column(types.String(255))
    name: Mapped[Optional[str]] = mapped_column(types.String(70))
    surname: Mapped[Optional[str]] = mapped_column(types.String(70))
    user_id: Mapped[UUID] = mapped_column(types.UUID, ForeignKey("users.id", ondelete="CASCADE"))
    user = relationship("User", back_populates="profiles")
    created_at: Mapped[datetime] = mapped_column(types.DateTime(), default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(types.DateTime(), nullable=True, default=None, onupdate=datetime.utcnow)
