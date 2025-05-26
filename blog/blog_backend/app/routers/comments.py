from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.database import get_db
from app.models.comment import Comment
from app.models.user import User
from app.schemas.comment import CommentCreate,CommentResponse
from app.dependencies import get_current_user
from app.utils.pagination import paginate, PaginatedResponse

router = APIRouter(prefix="/comments", tags=["comments"])

@router.post("/", response_model=CommentResponse,summary="创建评论")
def create_comment(
    comment_data: CommentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    comment = Comment(**comment_data.model_dump(), user_id=current_user.id)
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment

@router.get("/article/{article_id}", response_model=PaginatedResponse[CommentResponse],summary="查看分页的评论")
def get_article_comments(
    article_id: int,
    page: int = 1,
    page_size: int = 10,
    db: Session = Depends(get_db)
):
    # query = db.query(Comment).filter(Comment.article_id == article_id)
    query = db.exec(
        select(Comment).where(Comment.article_id == article_id)
    )
    return paginate(query, page, page_size, CommentResponse)