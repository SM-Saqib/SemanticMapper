

from pydantic import BaseModel
from datetime import datetime

class MappingBase(BaseModel):
    MappingId: int
    ProjectId: int

class MappingCreate(MappingBase):
    id : int

    CreatedAt: datetime = datetime.now()
    UpdatedAt: datetime = datetime.now()

class MappingUpdate(MappingBase):
    UpdatedAt: datetime = datetime.now()

class MappingInDB(MappingBase):
    id : int
    CreatedAt: datetime
    UpdatedAt: datetime

