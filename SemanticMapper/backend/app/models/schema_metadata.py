



from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON
from sqlalchemy.sql import func
from app.db.base_class import Base

class SchemaMetadata(Base):
    SchemaMetadataId = Column(Integer, primary_key=True)
    SchemaId = Column(Integer, ForeignKey('user_schemas.SchemaId'), nullable=False)
    ProjectId = Column(Integer, ForeignKey('projects.ProjectId'), nullable=False)
    Metadata = Column(JSON, nullable=False)
    CreatedAt = Column(DateTime, server_default=func.now())
    UpdatedAt = Column(DateTime, onupdate=func.now())
