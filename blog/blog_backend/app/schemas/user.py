from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str
    model_config = {
        "json_schema_extra":{
            "examples":[
                {
                    "username": "itop",
                    "email": "1871038859@qq.com",
                    "password": "123456"
                }
            ]
        }
    }

class UserLogin(BaseModel):
    username: str
    password: str

class UserUpdate(BaseModel):
    avatar: Optional[str] = None
    bio: Optional[str] = None

class PasswordUpdate(BaseModel):
    old_password: str
    new_password: str

class UserResponse(UserBase):
    id: int
    is_active: bool
    avatar: Optional[str]
    bio: Optional[str]

    class Config:
        from_attributes = True