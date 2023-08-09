


from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.db.base_class import Base


class UserSchema(Base):
    __tablename__ = 'user_schemas'
    SchemaId = Column(Integer, primary_key=True)
    ProjectId = Column(Integer, ForeignKey('projects.ProjectId'), nullable=False)
    SchemaName = Column(String(255), nullable=False)
    CreatedAt = Column(DateTime, server_default=func.now())
    UpdatedAt = Column(DateTime, onupdate=func.now())
    RawSchema = Column(String(255), nullable=False)
    