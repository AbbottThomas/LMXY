from typing import Generic, TypeVar
from pydantic import BaseModel

# 分页逻辑


T = TypeVar('T')

class PaginatedResponse(BaseModel, Generic[T]):
    page: int
    page_size: int
    total: int
    items: list[T]

def paginate(query, page: int, page_size: int, schema):
    total = query.count()
    items = query.offset((page - 1) * page_size).limit(page_size).all()
    return PaginatedResponse(
        page=page,
        page_size=page_size,
        total=total,
        items=[schema.model_validate(item) for item in items]
    )