from typing import Annotated

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from src.auth.utils import decode_jwt_token

security = HTTPBearer()


def must_be_logged_in(
        auth: Annotated[HTTPAuthorizationCredentials, Depends(security)]
) -> None:
    decode_jwt_token(auth.credentials)
