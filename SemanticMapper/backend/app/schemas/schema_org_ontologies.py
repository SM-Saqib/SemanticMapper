

from pydantic import BaseModel
from datetime import datetime

class SchemaOrgOntologyBase(BaseModel):
    OntologyId: int
    Version: str
    OntologyData: dict

class SchemaOrgOntologyCreate(SchemaOrgOntologyBase):
    id : int

    CreatedAt: datetime = datetime.now()
    UpdatedAt: datetime = datetime.now()

class SchemaOrgOntologyUpdate(SchemaOrgOntologyBase):
    UpdatedAt: datetime = datetime.now()

class SchemaOrgOntologyInDB(SchemaOrgOntologyBase):
    id : int
    CreatedAt: datetime
    UpdatedAt: datetime
