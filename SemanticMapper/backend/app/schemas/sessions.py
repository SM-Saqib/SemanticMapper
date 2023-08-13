

from pydantic import BaseModel
from datetime import datetime,timedelta

class SessionBase(BaseModel):
    SessionId: int
    UserId: int

class SessionCreate(SessionBase):
    id : int

    CreatedAt: datetime = datetime.now()
    ExpiresAt: datetime = datetime.now() + timedelta(days=1)
    UpdatedAt: datetime = datetime.now()

class SessionUpdate(SessionBase):
    UpdatedAt: datetime = datetime.now()

class SessionInDB(SessionBase):
    id : int
    CreatedAt: datetime
    ExpiresAt: datetime
    UpdatedAt: datetime
    