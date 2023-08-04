# 1.1 POST /api/v1/project/create
# Purpose: Create a new project and return a unique ProjectId.
# Input Parameters: None.
# Output:
# projectId (string) - Unique ProjectId for the newly created project.
# Error Handling:
# 500 Internal Server Error if there is a server-side error when creating the project.

# create the above API using fastapi, include all imports and dependencies

# backend/app/api.py
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from typing import Dict

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")  # Use your actual token endpoint URL

# Function to simulate project creation and return a unique projectId
def create_project() -> str:
    # Your actual logic for creating a new project goes here
    new_project_id = "some_unique_project_id"
    return new_project_id

@router.post("/api/v1/project/create", tags=["Project Management APIs"])
async def create_new_project(project_data: Dict,):
    # You can access the authenticated user using the token
    # Your OAuth2 validation logic goes here


    try:
        # Call the function to create the project and get the projectId
        project_id = create_project()

        # Return the projectId as response
        return {"projectId": project_id}

    except Exception as e:
        # If there is a server-side error, return a 500 Internal Server Error
        raise HTTPException(status_code=500, detail="Internal Server Error")
