from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.database.engine import get_db

from .models import Post
from .schemas import PostCreate, PostRead, PostUpdate

router = APIRouter()


@router.get("/posts", response_model=list[PostRead])
def get_posts(db: Session = Depends(get_db)):
    return db.query(Post).all()


@router.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post_in: PostCreate, db: Session = Depends(get_db)):
    post = Post(content=post_in.content)
    db.add(post)
    db.commit()


@router.get("/posts/{post_id}", status_code=status.HTTP_200_OK)
def get_post(post_id: UUID, db: Session = Depends(get_db)):
    return db.query(Post).get(post_id)


@router.put("/posts/{post_id}", status_code=status.HTTP_200_OK)
def update_post(post_id: UUID, post_in: PostUpdate, db: Session = Depends(get_db)):
    post = db.query(Post).get(post_id)
    if post is None:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

    for key, value in post_in.model_dump().items():
        setattr(post, key, value)

    db.commit()
