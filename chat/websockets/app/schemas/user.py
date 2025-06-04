from pydantic import BaseModel,EmailStr, Field,SecretStr,ConfigDict

class UserBase(BaseModel):
    # username: str=Field(alias="name")
    username: str
    email: EmailStr

class UserCreate(UserBase):
    # password: SecretStr=Field(min_length=6,max_length=12)
    password: str=Field(min_length=6,max_length=12)
    model_config = ConfigDict(json_schema_extra={
               "examples":[
                {
                    "username": "Jay",
                    "email": "Jay@qq.com",
                     "password": "123456"
                }     
               ]
    })
    
class UserLogin(BaseModel):
    username: str
    # password: SecretStr=Field(min_length=6,max_length=12)
    password: str=Field(min_length=6,max_length=12)
    
class PasswordUpdate(BaseModel):
    # old_password: SecretStr=Field(min_length=6,max_length=12)
    # new_password: SecretStr=Field(min_length=6,max_length=12)
    old_password: str=Field(min_length=6,max_length=12)
    new_password: str=Field(min_length=6,max_length=12)
    
class UserResponse(UserBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
    