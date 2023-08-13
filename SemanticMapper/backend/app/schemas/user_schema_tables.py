

from pydantic import BaseModel
from datetime import datetime

class UserSchemaTableBase(BaseModel):
    TableId: int
    SchemaId: int
    TableName: str

class UserSchemaTableCreate(UserSchemaTableBase):
    id : int
    CreatedAt: datetime = datetime.now()
    UpdatedAt: datetime = datetime.now()

class UserSchemaTableUpdate(UserSchemaTableBase):
    UpdatedAt: datetime = datetime.now()
    

class UserSchemaTableInDB(UserSchemaTableBase):
    id : int
    CreatedAt: datetime
    UpdatedAt: datetime
    