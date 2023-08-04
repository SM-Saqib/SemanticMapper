from app.endpoints import project_management
from fastapi import APIRouter

router = APIRouter()

# Include the router for your APIs

router.include_router(router = project_management.router, tags=["Project Management APIs"])

