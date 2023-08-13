

from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    UserId: int
    Email: str
    PasswordHash: str
    FirstName: str
    LastName: str

class UserCreate(UserBase):
    id : int
    CreatedAt: datetime = datetime.now()
    UpdatedAt: datetime = datetime.now()

class UserUpdate(UserBase):
    UpdatedAt: datetime = datetime.now()

class UserInDB(UserBase):
    id : int
    CreatedAt: datetime
    UpdatedAt: datetime
    