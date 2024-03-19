from pydantic import EmailStr, SecretStr

from src.core.base_schema import CustomBaseModel


class UserRegister(CustomBaseModel):
    email: EmailStr
    password: SecretStr


class UserLogin(CustomBaseModel):
    email: EmailStr
    password: SecretStr


class UserRead(CustomBaseModel):
    email: EmailStr


class Token(CustomBaseModel):
    token: str


class TokenResponse(CustomBaseModel):
    access_token: str
    refresh_token: str
    token_type: str
