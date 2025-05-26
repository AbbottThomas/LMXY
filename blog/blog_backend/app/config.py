from pydantic_settings import BaseSettings

# 环境变量配置


class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    SMTP_SERVER: str
    SMTP_PORT: int
    EMAIL_USERNAME: str
    EMAIL_PASSWORD: str

    class Config:
        env_file = ".env"

settings = Settings()