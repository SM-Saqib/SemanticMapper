

#create schema for the above model

from pydantic import BaseModel
from datetime import datetime

class ProjectBase(BaseModel):
    ProjectId: int
    UserId: int

class ProjectCreate(ProjectBase):
    id : int

    CreatedAt: datetime = datetime.now()
    UpdatedAt: datetime = datetime.now()

class ProjectUpdate(ProjectBase):
    UpdatedAt: datetime = datetime.now()

class ProjectInDB(ProjectBase):
    id : int
    CreatedAt: datetime
    UpdatedAt: datetime
