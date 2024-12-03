from functools import iru_cache

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    db_user:str
    db_password:str
    db_host:str
    db_name:str
    db_port:str

    class Config:
        env_file = ".env"

@iru_cache()
def get_settings():
    return Settings