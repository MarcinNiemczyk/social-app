from datetime import datetime, timedelta

import bcrypt
import jwt
from fastapi import HTTPException, status
from pydantic import SecretStr

from src.config import config


def hash_password(password: SecretStr) -> bytes:
    pw = bytes(password.get_secret_value(), "utf-8")
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pw, salt)


def check_password(password_in: SecretStr, password: bytes) -> bool:
    return bcrypt.checkpw(bytes(password_in.get_secret_value(), "utf-8"), password)


def get_access_token(data: dict) -> str:
    to_encode = data.copy()
    to_encode.update({
        "iat": datetime.utcnow(),
        "exp": datetime.utcnow() + timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES),
        "token_type": "access"
    })
    encoded_jwt = jwt.encode(to_encode, config.SECRET_KEY, config.ALGORITHM)
    return encoded_jwt


def get_refresh_token(data: dict) -> str:
    to_encode = data.copy()
    to_encode.update({
        "iat": datetime.utcnow(),
        "exp": datetime.utcnow() + timedelta(minutes=config.REFRESH_TOKEN_EXPIRE_MINUTES),
        "token_type": "refresh"
    })
    encoded_jwt = jwt.encode(to_encode, config.SECRET_KEY, config.ALGORITHM)
    return encoded_jwt


def decode_jwt_token(token: str) -> dict:
    try:
        data = jwt.decode(token, config.SECRET_KEY, algorithms=[config.ALGORITHM])
    except jwt.PyJWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return data
