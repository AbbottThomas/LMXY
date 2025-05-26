from fastapi import APIRouter, Depends, HTTPException,Body,status
from sqlmodel import Session,select
from app.database import get_db
from fastapi.security import OAuth2PasswordRequestForm

from app.models.user import User
from app.schemas.user import UserCreate, UserLogin
from app.utils.security import get_password_hash, verify_password, create_access_token

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

# @router.post("/register",summary="register函数",description="""**邮箱注册**""",
@router.post("/register",summary="register函数",
             responses={
                 status.HTTP_201_CREATED:{"description": "成功创建用户"},
                 status.HTTP_400_BAD_REQUEST:{"description":"Username or email already exists"}
             }
             )
def register(user: UserCreate, db: Session = Depends(get_db)):
    """
    邮箱注册用户

    Args:  
    - user (UserCreate): 用户信息  
        - email
        - username
        - password
    - db (Session, optional): 数据库连接会话. Defaults to Depends(get_db).

    Raises:  
        HTTPException: 400

    Returns:  
        200: 默认
    """
    existing_user = db.exec(
        select(User).where(
            (User.username == user.username) | (User.email == user.email)
        )
    ).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username or email already exists")
    
    hashed_password = get_password_hash(user.password)
    db_user = User(**user.model_dump(exclude={"password"}), hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": "User created successfully"}

@router.post("/login",summary="用户密码登录")
def login(credentials: OAuth2PasswordRequestForm=Depends(), db: Session = Depends(get_db)):
    user = db.exec(
        select(User).where(
            User.username == credentials.username
        )
    ).first()
    """
    用户密码登录

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    if not user or not verify_password(credentials.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}