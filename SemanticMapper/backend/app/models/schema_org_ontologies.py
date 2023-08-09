


from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func

from app.db.base_class import Base

class SchemaOrgOntology(Base):
    __tablename__ = 'schema_org_ontologies'
    OntologyId = Column(Integer, primary_key=True)
    Version = Column(String(255), nullable=False)
    OntologyData = Column(JSONB, nullable=False)
    CreatedAt = Column(DateTime, server_default=func.now())
    UpdatedAt = Column(DateTime, onupdate=func.now())