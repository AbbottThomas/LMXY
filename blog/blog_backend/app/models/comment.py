from sqlmodel import SQLModel, Field, Relationship
from typing import Optional,TYPE_CHECKING
from datetime import datetime,timezone
if TYPE_CHECKING:
    from app.models.user import User
    from app.models.article import Article

class CommentBase(SQLModel):
    content: str = Field(max_length=500)
    created_at: datetime = Field(default_factory=datetime.now(timezone.utc))
    parent_comment_id: Optional[int] = None

class Comment(CommentBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    article_id: int = Field(foreign_key="article.id")
    
    user: "User" = Relationship(back_populates="comments")
    article: "Article" = Relationship(back_populates="comments")