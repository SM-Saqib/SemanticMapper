from app.endpoints import (
    project_management,
    file_upload_management,
    semantic_mapping
)
from fastapi import APIRouter

api_router = APIRouter()

# Include the router for your APIs

api_router.include_router(project_management.router, prefix="/project", tags=["Project Management APIs"])
api_router.include_router(file_upload_management.router, prefix="/file", tags=["File Upload Management APIs"])
api_router.include_router(semantic_mapping.router, prefix="/mapping", tags=["Semantic Mapping APIs"])

