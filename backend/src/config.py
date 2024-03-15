import logging
import os

from pydantic_settings import BaseSettings, SettingsConfigDict

log = logging.getLogger(__name__)

DOTENV = os.path.join(os.path.dirname(__file__), ".env")


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file=DOTENV, env_file_encoding="utf-8")
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int


config = Config()  # type: ignore
if not config.SECRET_KEY:
    log.warning("No JWT Secret specified. Authentication system is suppressed.")
