from src.post.interfaces.repository import IPostRepository


class PostService:
    def __init__(self, repository: IPostRepository):
        self.repository = repository
