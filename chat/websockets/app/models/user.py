from typing import TYPE_CHECKING
from sqlmodel import Column, Field, SQLModel, String
from pydantic import EmailStr

class User(SQLModel,table=True):
    # __tablename__ = "user"
    __table_args__ = {"extend_existing": True}
    id: int | None = Field(default=None,primary_key=True)
    username: str = Field(sa_column=Column(String(50),index=True))
    email: EmailStr=Field(unique=True)
    password: str = Field(min_length=6,max_length=12)
    # hashed_password: str
    # salt: str
    