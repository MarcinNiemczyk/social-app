import uvicorn
from fastapi import FastAPI
from src.database.engine import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"hello": "world"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
