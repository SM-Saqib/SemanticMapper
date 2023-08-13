

from pydantic import BaseModel
from datetime import datetime

class SchemaOrgTermBase(BaseModel):
    TermId: int
    OntologyId: int
    TermURI: str
    TermName: str
    TermDefinition: str

class SchemaOrgTermCreate(SchemaOrgTermBase):
    id : int
    CreatedAt: datetime = datetime.now()
    UpdatedAt: datetime = datetime.now()

class SchemaOrgTermUpdate(SchemaOrgTermBase):
    UpdatedAt: datetime = datetime.now()


class SchemaOrgTermInDB(SchemaOrgTermBase):
    id : int
    CreatedAt: datetime
    UpdatedAt: datetime
    