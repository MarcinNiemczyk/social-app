from pydantic import BaseModel, EmailStr, SecretStr


class UserRegister(BaseModel):
    email: EmailStr
    password: SecretStr


class UserLogin(BaseModel):
    email: EmailStr
    password: SecretStr


class UserRead(BaseModel):
    email: EmailStr
