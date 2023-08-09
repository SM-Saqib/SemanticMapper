#./app/endpoints/accessing_schema_metadata.py
from fastapi import APIRouter, HTTPException, Depends
from app.crud.crud_accessing_schema_metadata import crud_accessing_schema_metadata
router = APIRouter()

@router.get("/metadata/{projectId}", tags=["Metadata APIs"])
async def get_metadata(projectId: str):
    '''
    Purpose: Retrieve metadata and enrichments loaded with schema for a project.
    Input Parameters:
    projectId (string, in URL) - The unique identifier of the project.
    Output:
    metadata (object) - Contains schema metadata like descriptions, examples, links etc.
    Error Handling:
    404 Not Found if invalid projectId provided.
    500 Internal Server Error if error retrieving metadata.
    
    '''
    try:
        # retrieve metadata and return the status
        # return {"status": "success", "message": "Metadata retrieved successfully"}

        #use app.crud.crud_accessing_schema_metadata to retrieve metadata

        metadata =
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
