from pydantic import BaseModel, Field
from typing import Optional

class CategoryBase(BaseModel):
    name: str = Field(..., max_length=50)
    description: Optional[str] = Field(None, max_length=200)

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(CategoryBase):
    name: Optional[str] = Field(None, max_length=50)
    description: Optional[str] = Field(None, max_length=200)

class CategoryResponse(CategoryBase):
    id: int
    article_count: int = 0  # 通过关系自动计算

    class Config:
        from_attributes = True