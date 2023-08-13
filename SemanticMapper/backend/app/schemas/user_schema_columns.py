

from pydantic import BaseModel
from datetime import datetime

class UserSchemaColumnBase(BaseModel):
    ColumnId: int
    TableId: int
    ColumnName: str
    DataType: str
    SchemaOrgTermId: int

class UserSchemaColumnCreate(UserSchemaColumnBase):
    id : int
    CreatedAt: datetime = datetime.now()
    UpdatedAt: datetime = datetime.now()

class UserSchemaColumnUpdate(UserSchemaColumnBase):
    UpdatedAt: datetime = datetime.now()


class UserSchemaColumnInDB(UserSchemaColumnBase):
    id : int
    CreatedAt: datetime
    UpdatedAt: datetime
    