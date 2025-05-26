from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List,TYPE_CHECKING
if TYPE_CHECKING:
    from app.models.article import Article  

class CategoryBase(SQLModel):
    name: str = Field(index=True, unique=True, max_length=50)
    description: str = Field(max_length=200)

class Category(CategoryBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    articles: List["Article"] = Relationship(back_populates="category")