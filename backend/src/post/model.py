from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import types
from sqlalchemy.orm import Mapped, mapped_column

from src.database.engine import Base


class Post(Base):
    __tablename__ = "posts"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    content: Mapped[str] = mapped_column(types.String(255))
    created_at: Mapped[datetime] = mapped_column(types.DateTime(), default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(types.DateTime(), nullable=True, default=None, onupdate=datetime.utcnow)
    scope: Mapped[str] = mapped_column(types.String(20), default="global")
    status: Mapped[str] = mapped_column(types.String(20), default="active")
