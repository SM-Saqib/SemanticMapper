


from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

from sqlalchemy.sql import func
from app.db.base_class import Base

class UserSchemaTable(Base):
    __tablename__ = 'user_schema_tables'
    TableId = Column(Integer, primary_key=True)
    SchemaId = Column(Integer, ForeignKey('user_schemas.SchemaId'), nullable=False)
    TableName = Column(String(255), nullable=False)
    CreatedAt = Column(DateTime, server_default=func.now())
    UpdatedAt = Column(DateTime, onupdate=func.now())