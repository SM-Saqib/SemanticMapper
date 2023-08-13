

from pydantic import BaseModel
from datetime import datetime

class MappingDetailBase(BaseModel):
    DetailId: int
    MappingId: int
    ColumnId: int
    TermId: int
    AutoGenerated: bool
    Curated: bool
    Certainty: str
    Reasoning: str
    

class MappingDetailCreate(MappingDetailBase):
    id : int
    CreatedAt: datetime = datetime.now()
    UpdatedAt: datetime = datetime.now()

class MappingDetailUpdate(MappingDetailBase):
    UpdatedAt: datetime = datetime.now()
    

class MappingDetailInDB(MappingDetailBase):
    id : int
    CreatedAt: datetime
    UpdatedAt: datetime
