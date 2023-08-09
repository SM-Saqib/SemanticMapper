

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func

from app.db.base_class import Base

class Mapping(Base):
    __tablename__ = 'mappings'
    MappingId = Column(Integer, primary_key=True)
    ProjectId = Column(Integer, ForeignKey('projects.ProjectId'), nullable=False)
    CreatedAt = Column(DateTime, server_default=func.now())
    UpdatedAt = Column(DateTime, onupdate=func.now())