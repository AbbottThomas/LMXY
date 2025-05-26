from pydantic import BaseModel
from datetime import datetime
from app.schemas.user import UserResponse

class CommentBase(BaseModel):
    content: str
    article_id: int

class CommentCreate(CommentBase):
    pass

class CommentResponse(CommentBase):
    id: int
    created_at: datetime
    user: UserResponse

    class Config:
        from_attributes = True