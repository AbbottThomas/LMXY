from pydantic_settings import BaseSettings,SettingsConfigDict
import os
from functools import lru_cache
from typing import Optional



class Settings(BaseSettings):
    DATABASE_URL: str = "mysql+pymysql://user:password@localhost/blog_db"
    SECRET_KEY: str = "123456"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    # SMTP_SERVER: Optional[str]
    # SMTP_PORT: Optional[int]
    # EMAIL_USERNAME: Optional[str]
    # EMAIL_PASSWORD: Optional[str]
    
    # class Config:
    #     env_file = "./env"



settings = Settings()   

# @lru_cache
# def get_settings():
#     return Settings()


