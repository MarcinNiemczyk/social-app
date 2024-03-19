from pydantic import EmailStr

from src.core.base_schema import CustomBaseModel


class UserCreate(CustomBaseModel):
    email: EmailStr
    password: bytes
