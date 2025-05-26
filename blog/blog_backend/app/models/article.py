from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List,TYPE_CHECKING
from datetime import datetime,timezone

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.category import Category
    from app.models.comment import Comment

class ArticleBase(SQLModel):
    title: str = Field(index=True, max_length=200)
    content: str
    published_at: datetime = Field(default_factory=datetime.now(timezone.utc))
    is_published: bool = False

class Article(ArticleBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    author_id: int = Field(foreign_key="user.id")
    category_id: int = Field(foreign_key="category.id")
    
    author: "User" = Relationship(back_populates="articles")
    category: "Category" = Relationship(back_populates="articles")
    comments: List["Comment"] = Relationship(back_populates="article")