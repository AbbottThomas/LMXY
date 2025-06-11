from pydantic import EmailStr,SecretStr
from sqlmodel import SQLModel,Field
from enums import UserType,UserStatus
import phonenumbers 
from datetime import datetime,timezone



class User(SQLModel,table=True):
    __table_args__ = {"extend_existing": True}
    id: int|None=Field(default=None,primary_key=True)
    serial: str=Field(unique=True,index=True)
    username: str=Field()
    type: UserType
    email: EmailStr|None
    phone: str|None = Field(max_length=20, index=True)
    password_hash: SecretStr = Field(max_length=128)
    salt: str = Field(max_length=32)
    create_at: datetime = Field(default_factory=datetime.now)
    last_login: datetime|None = None
    status: UserStatus = Field(default=UserStatus.online)
    
    