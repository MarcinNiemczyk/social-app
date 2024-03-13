import bcrypt
from pydantic import SecretStr


def hash_password(password: SecretStr) -> bytes:
    pw = bytes(password.get_secret_value(), "utf-8")
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pw, salt)


def check_password(password_in: SecretStr, password: bytes) -> bool:
    return bcrypt.checkpw(bytes(password_in.get_secret_value(), "utf-8"), password)
