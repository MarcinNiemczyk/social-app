from typing import Annotated
from uuid import UUID

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from src.auth.utils import decode_jwt_token

security = HTTPBearer()


def must_be_logged_in(
        auth: Annotated[HTTPAuthorizationCredentials, Depends(security)]
) -> None:
    decode_jwt_token(auth.credentials)


def get_user_id_from_token(
        auth: Annotated[HTTPAuthorizationCredentials, Depends(security)]
) -> UUID:
    token = decode_jwt_token(auth.credentials)
    return UUID(token.get("sub"))
