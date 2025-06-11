from sqlmodel import SQLModel, Field, Relationship
from .user import User

class UserPrivilege(SQLModel, table=True):
    # __tablename__ = "user_privilege"   
    id: int|None = Field(default=None, primary_key=True)
    invitation_code_num: int = Field(default=10)
    create_invitation: bool = Field(default=False)
    anonymous_num: int = Field(default=5)
    create_anonymous: bool = Field(default=False)
    relation_gap: int = Field(default=3)
    
    user_id: int = Field(foreign_key="user.id", index=True)
    user: User = Relationship(back_populates="privileges")