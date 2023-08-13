

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class SchemaMetadataBase(BaseModel):
    SchemaMetadataId: Optional[int]
    SchemaId: int
    ProjectId: int
    Metadata: dict

class SchemaMetadataCreate(SchemaMetadataBase):
    CreatedAt: datetime = Field(default_factory=datetime.utcnow)
    UpdatedAt: datetime = Field(default_factory=datetime.utcnow)


class SchemaMetadataUpdate(SchemaMetadataBase):
    UpdatedAt: datetime = Field(default_factory=datetime.utcnow)

class SchemaMetadataInDB(SchemaMetadataBase):
    id : int
    CreatedAt: datetime
    UpdatedAt: datetime