from pydantic import ConfigDict, EmailStr, SecretStr

from src.core.base_schema import CustomBaseModel


class UserRegister(CustomBaseModel):
    email: EmailStr
    password: SecretStr

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "email": "user@example.com",
                "password": "Password123!",
            },
        }
    )


class UserLogin(CustomBaseModel):
    email: EmailStr
    password: SecretStr

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "email": "user@example.com",
                "password": "Password123!",
            },
        }
    )


class UserRead(CustomBaseModel):
    email: EmailStr


class Token(CustomBaseModel):
    token: str


class TokenResponse(CustomBaseModel):
    access_token: str
    refresh_token: str
    token_type: str
