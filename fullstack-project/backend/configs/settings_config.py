from pydantic_settings import BaseSettings
from pydantic import Field
# from functools import lru_cache
# from dotenv import load_dotenv


# load_dotenv(".env")

class Settings(BaseSettings):
    # DATABASE_URL: str = "mysql+pymysql://user:password@localhost/blog_db"
    MYSQL_URI: str = Field()
    MONGODB_URI: str = Field()
    REDIS_URI: str = Field()
    
    # ALGORITHM: str = Field(default="HS256")
    # ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Fastapi运行的当前工作目录，可能不是backend/configs，因此直接.env无法找到
    # 可以将.env放入fastapi的根目录同main.py同级
    # 可以用load_dotenv("")加载环境变量，从Config类读取的要求字段严格一致，而加载的可以大于定义字段
    # env_file使用绝对目录或者相对目录根据工作目录main.py来
    # 工作目录就是当前输入fastapi dev main.py的目录
    class Config:
        env_file = "./configs/.env"
        env_file_encoding = "utf-8"
        # extra = "allow"

settings = Settings()   # type: ignore

# @lru_cache
# def get_settings():
#     return Settings()


