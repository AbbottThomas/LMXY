from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from app.database import get_db
from app.models.user import User
from app.schemas.user import UserUpdate, UserResponse, PasswordUpdate
from app.dependencies import get_current_user
from app.utils.security import get_password_hash, verify_password

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/me", response_model=UserResponse,summary="根据token,获得当前用户")
def get_current_user_profile(current_user: User = Depends(get_current_user)):
    """

    Args:
    - current_user (User, optional): 用户模型. 
    - Defaults to Depends(get_current_user).

    Returns:
        当前用户: 当前用户模型
    """
    return current_user

@router.patch("/me", response_model=UserResponse,summary="更新部分用户简介")
def update_user_profile(
    user_data: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """update_user_profile

    Args:
        user_data (UserUpdate): 用户数据模型
        db (Session, optional): 连接数据库的会话. Defaults to Depends(get_db).
        current_user (User, optional): 根据tkekn获取当前用户的多重依赖. Defaults to Depends(get_current_user).

    Returns:
        current_user: 更新后的用户表模型
    """
    update_data = user_data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(current_user, key, value)
    db.add(current_user)
    db.commit()
    db.refresh(current_user)
    return current_user

@router.post("/change-password",summary="更改密码")
def change_password(
    password_data: PasswordUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if not verify_password(password_data.old_password, current_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Old password is incorrect"
        )
    
    current_user.hashed_password = get_password_hash(password_data.new_password)
    db.add(current_user)
    db.commit()
    return {"message": "Password updated successfully"}