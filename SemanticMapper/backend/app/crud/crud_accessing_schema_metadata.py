
from app.crud.crud_base import CRUDBase
from app.models.schema_metadata import SchemaMetadata
from app.schemas.schema_metadata import SchemaMetadataBase, SchemaMetadataCreate, SchemaMetadataUpdate


class CRUDAccessingSchemaMetadata(CRUDBase):
    pass

crud_accessing_schema_metadata = CRUDAccessingSchemaMetadata(SchemaMetadata,[SchemaMetadataCreate, SchemaMetadataUpdate])