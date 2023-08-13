from sqlalchemy.orm import Session
from typing import Type, List, Optional
from pydantic import BaseModel


class CRUDBase():
    def __init__(self, model: Type[BaseModel], schema: Type[BaseModel]):
        self.model = model
        self.schema = schema

    def create(self, db: Session, obj_in: BaseModel) -> BaseModel:
        db_obj = self.model(**obj_in.__dict__() if isinstance(obj_in, BaseModel) else obj_in)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get(self, db: Session, id: int) -> Optional[BaseModel]:
        return db.query(self.model).filter(self.model.id == id).first()

    def get_multi(self, db: Session, skip: int = 0, limit: int = 10) -> List[BaseModel]:
        return db.query(self.model).offset(skip).limit(limit).all()

    def update(self, db: Session, db_obj: BaseModel, obj_in: BaseModel) -> BaseModel:
        for var, value in obj_in:
            setattr(db_obj, var, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, id: int) -> BaseModel:
        obj = db.query(self.model).get(id)
        db.delete(obj)
        db.commit()
        return obj