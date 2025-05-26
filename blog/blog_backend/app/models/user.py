from sqlmodel import SQLModel, Field,Relationship
from typing import Optional, List, TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.article import Article  # 避免循环导入
    from app.models.comment import Comment

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True, max_length=50)
    email: str = Field(index=True, unique=True, max_length=100)
    hashed_password: str
    is_active: bool = Field(default=False)
    avatar: Optional[str] = None
    bio: Optional[str] = Field(max_length=200, default=None)
    
    articles: List["Article"] = Relationship(back_populates="author")
    comments: List["Comment"] = Relationship(back_populates="user")