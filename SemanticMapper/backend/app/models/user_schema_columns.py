

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.db.base_class import Base

class UserSchemaColumn(Base):
    __tablename__ = 'user_schema_columns'
    ColumnId = Column(Integer, primary_key=True)
    TableId = Column(Integer, ForeignKey('user_schema_tables.TableId'), nullable=False)
    ColumnName = Column(String(255), nullable=False)
    DataType = Column(String(255), nullable=False)
    SchemaOrgTermId = Column(Integer, ForeignKey('schema_org_terms.TermId'))
    CreatedAt = Column(DateTime, server_default=func.now())
    UpdatedAt = Column(DateTime, onupdate=func.now())