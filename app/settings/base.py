from pydantic_settings import BaseSettings, SettingsConfigDict

from app.utils.get_path import get_path


class Settings(BaseSettings):
    token: str

    model_config = SettingsConfigDict(env_file=get_path(".env"), env_nested_delimiter="__")