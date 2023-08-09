


from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.db.base_class import Base

class Session(Base):
    __tablename__ = 'sessions'
    SessionId = Column(Integer, primary_key=True)
    UserId = Column(Integer, ForeignKey('users.UserId'), nullable=False)
    CreatedAt = Column(DateTime, server_default=func.now())
    ExpiresAt = Column(DateTime, nullable=False)
    UpdatedAt = Column(DateTime, onupdate=func.now())