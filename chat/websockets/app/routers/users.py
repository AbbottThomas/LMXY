from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy import select
from sqlmodel import select
from app.databases.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate,UserLogin
from fastapi import APIRouter,Depends,HTTPException,status

router = APIRouter(prefix="/users",tags=["users"])

@router.post("/register")
async def register(user:UserCreate,db:AsyncSession=Depends(get_db)):
    """
    用户注册  

    Args:  
        user (UserCreate): 用户请求体  
        db (AsyncSession, optional): 异步会话连接. Defaults to Depends(get_db).  
    """
    stmt = select(User).where((User.username==user.username)|(User.email==user.email))
    result = await db.execute(stmt)
    existing_user = result.first()
    if existing_user:
        raise HTTPException(status_code=400,detail="Username or email already exists")
    new_user = User(**user.model_dump())
    db.add(new_user)
    await db.commit()
    return new_user
