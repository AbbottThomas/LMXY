from pydantic import BaseModel
from datetime import datetime
from app.schemas.user import UserResponse
from app.schemas.category import CategoryResponse

class ArticleBase(BaseModel):
    title: str
    content: str

class ArticleCreate(ArticleBase):
    category_id: int

class ArticleResponse(ArticleBase):
    id: int
    published_at: datetime
    author: UserResponse
    category: CategoryResponse

    class Config:
        from_attributes = True