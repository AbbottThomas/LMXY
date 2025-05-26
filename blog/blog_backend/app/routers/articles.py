from fastapi import APIRouter, Depends, UploadFile, File,HTTPException
from sqlmodel import Session
from app.database import get_db
from app.models.article import Article
from app.schemas.article import ArticleCreate
from app.dependencies import get_current_user
from app.models.user import User

router = APIRouter(
    prefix="/articles",
    tags=["articles"],
)

# 需要新增的功能：
# 1. 获取用户的所有文章标题及id，并分页展示
# 2. 通过搜索文章标题名，返回文章标题和id
# 3. 通过分类，返回标准标题和id




@router.post("/",summary="新建文章")
def create_article(
    article: ArticleCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_article = Article(**article.model_dump(), author_id=current_user.id)
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article

@router.get("/",summary="获取文章列表")
def get_articles(
    
):
    return


@router.get("/{article_id}",summary="通过文章id查看文章")
def get_article(article_id: int, db: Session = Depends(get_db)):
    article = db.get(Article, article_id)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article