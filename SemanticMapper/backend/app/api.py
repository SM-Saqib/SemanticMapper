from app.endpoints import (
    project_management,
    file_upload_management,
    semantic_mapping,
    mapping_file_export,
    user_management,
    chat_interaction,
    session_verification,
    schema_org_ontology_retrieval,
    user_management,
    viewing_uploaded_schemas,
    accessing_schema_metadata,
    getting_target_metadata,

)
from fastapi import APIRouter

api_router = APIRouter()

# Include the router for your APIs

api_router.include_router(project_management.router, prefix="/project", tags=["Project Management APIs"])
api_router.include_router(file_upload_management.router, prefix="/file", tags=["File Upload Management APIs"])
api_router.include_router(semantic_mapping.router, prefix="/mapping", tags=["Semantic Mapping APIs"])
api_router.include_router(mapping_file_export.router, prefix="/export", tags=["Export APIs"])
api_router.include_router(user_management.router, prefix="/user", tags=["User Management APIs"])
api_router.include_router(chat_interaction.router, prefix="/chat", tags=["Chat Interaction APIs"])
api_router.include_router(session_verification.router, prefix="/session", tags=["Session Verification APIs"])
api_router.include_router(schema_org_ontology_retrieval.router, prefix="/ontology", tags=["Ontology APIs"])
api_router.include_router(user_management.router, prefix="/user", tags=["User Management APIs"])
api_router.include_router(viewing_uploaded_schemas.router, prefix="/schemas", tags=["Viewing Uploaded Schemas APIs"])
api_router.include_router(accessing_schema_metadata.router, prefix="/metadata", tags=["Accessing Schema Metadata APIs"])

api_router.include_router(getting_target_metadata.router, prefix="/ontology", tags=["Ontology APIs"])



