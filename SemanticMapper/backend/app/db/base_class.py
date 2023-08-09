import re
from datetime import datetime
from typing import Dict, Optional

from sqlalchemy import Column, Integer, inspect
from sqlalchemy.ext.declarative import as_declarative, declared_attr

class_registry: Dict = {}


@as_declarative(class_registry=class_registry)
class Base:
    id: int
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return re.sub(r'(?<!^)(?=[A-Z])', '_', cls.__name__).lower()

    @declared_attr
    def __table_args__(cls) -> Dict:
        return {'extend_existing': True}

    @declared_attr
    def __mapper_args__(cls) -> Dict:
        return {'eager_defaults': True}

    @property
    def pk(self) -> Optional[int]:
        return inspect(self).identity[0] if inspect(self).identity else None

    @property
    def created_at(self) -> Optional[datetime]:
        return getattr(self, 'CreatedAt', None)

    @property
    def updated_at(self) -> Optional[datetime]:
        return getattr(self, 'UpdatedAt', None)

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__}({self.pk})>'
    
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}