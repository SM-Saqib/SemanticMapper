
    
from pydantic import BaseModel
from datetime import datetime

class UserSchemaBase(BaseModel):
    SchemaId: int
    ProjectId: int
    SchemaName: str
    RawSchema: str


class UserSchemaCreate(UserSchemaBase):
    id : int
    CreatedAt: datetime = datetime.now()
    UpdatedAt: datetime = datetime.now()

class UserSchemaUpdate(UserSchemaBase):
    UpdatedAt: datetime = datetime.now()


class UserSchemaInDB(UserSchemaBase):
    id : int
    CreatedAt: datetime
    UpdatedAt: datetime
    