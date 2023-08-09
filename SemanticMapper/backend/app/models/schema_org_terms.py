

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.sql import func
from app.db.base_class import Base

class SchemaOrgTerm(Base):
    __tablename__ = 'schema_org_terms'
    TermId = Column(Integer, primary_key=True)
    OntologyId = Column(Integer, ForeignKey('schema_org_ontologies.OntologyId'), nullable=False)
    TermURI = Column(String(255), nullable=False)
    TermName = Column(String(255), nullable=False)
    TermDefinition = Column(Text)
    CreatedAt = Column(DateTime, server_default=func.now())
    UpdatedAt = Column(DateTime, onupdate=func.now())
