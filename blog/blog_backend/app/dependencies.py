from fastapi import Depends, HTTPException, status,Request
from fastapi.security import OAuth2PasswordBearer
import  jwt
from jwt import ExpiredSignatureError
from sqlmodel import Session,select
from app.database import get_db
from app.models.user import User
from app.config import settings
# from app.schemas.user import UserLogin

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if not username:
            raise credentials_exception
    except ExpiredSignatureError:
        raise credentials_exception
    
    user = db.exec(
        select(User).where(
            User.username == username
        )
    ).first()
    if not user:
        raise credentials_exception
    return user



# 处理混合请求，但是不要这样做，添加复杂性没必要
# async def get_credentials(request: Request):
#     content_type = request.headers.get("content-type", "")
#     if "application/json" in content_type:
#         try:
#             json_data = await request.json()
#             return UserLogin(**json_data)
#         except:
#             raise HTTPException(400, "Invalid JSON")
#     elif "application/x-www-form-urlencoded" in content_type:
#         form_data = await request.form()
#         return OAuth2PasswordRequestForm(
#             username=form_data.get("username"),
#             password=form_data.get("password"),
#             scope=form_data.get("scope", ""),
#             # 其他可选字段
#         )
#     else:
#         raise HTTPException(415, "Unsupported media type")