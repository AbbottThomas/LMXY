from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.database import get_db
from app.models.category import Category
from app.models.user import User
from app.schemas.category import (
    CategoryCreate,
    CategoryUpdate,
    CategoryResponse
)
from app.dependencies import get_current_user

router = APIRouter(
    prefix="/categories",
    tags=["categories"],
    responses={404: {"description": "Not found"}}
)

@router.post("/", response_model=CategoryResponse,summary="创建分类")
def create_category(
    category: CategoryCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    # 检查分类名称是否已存在
    existing_category = db.exec(
        select(Category).where(Category.name == category.name)
    ).first()
    if existing_category:
        raise HTTPException(
            status_code=409,
            detail="Category name already exists"
        )
    
    db_category = Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

@router.get("/", response_model=list[CategoryResponse],summary="获得所有分类")
def get_all_categories(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100
):
    categories = db.exec(
        select(Category).offset(skip).limit(limit)
    ).all()
    return categories

@router.put("/{category_id}", response_model=CategoryResponse,summary="更新分类")
def update_category(
    category_id: int,
    category_data: CategoryUpdate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    db_category = db.get(Category, category_id)
    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")
    
    update_data = category_data.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_category, key, value)
    
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

@router.delete("/{category_id}",summary="删除分类")
def delete_category(
    category_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    db_category = db.get(Category, category_id)
    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")
    
    db.delete(db_category)
    db.commit()
    return {"message": "Category deleted successfully"}