

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.db.base_class import Base

class User(Base):
    __tablename__ = 'users'
    UserId = Column(Integer, primary_key=True)
    Email = Column(String(255), unique=True, nullable=False)
    PasswordHash = Column(String(255), nullable=False)
    FirstName = Column(String(255), nullable=False)
    LastName = Column(String(255), nullable=False)
    CreatedAt = Column(DateTime, server_default=func.now())
    UpdatedAt = Column(DateTime, onupdate=func.now())


