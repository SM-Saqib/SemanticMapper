# ./app/endpoints/project_management.py
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from typing import Dict

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")  # Use your actual token endpoint URL

# def create_project():
   


@router.post("/project/create", tags=["Project Management APIs"])
async def create_new_project(project_data: Dict,):
    try:
        # create a new project and return the projectId
        return {"status": "success", "projectId": 1}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
