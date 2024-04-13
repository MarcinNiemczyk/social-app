import uvicorn
from fastapi import FastAPI

from src.auth.views import auth_router
from src.database.engine import Base, engine
from src.post.views import post_router
from src.profile.views import profile_router

app = FastAPI()
app.include_router(auth_router, tags=["Authentication"])
app.include_router(profile_router, prefix="/profiles", tags=["Profiles"])
app.include_router(post_router, prefix="/posts", tags=["Posts"])

Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
