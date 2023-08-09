#./app/endpoints/getting_target_metadata.py

from fastapi import APIRouter, HTTPException, Depends

router = APIRouter()

@router.get("/ontology/metadata/{projectId}", tags=["Ontology APIs"])
async def get_target_metadata(projectId: str):
    '''
    Purpose: Retrieve schema.org metadata for target schema elements.
    Input Parameters:
    projectId (string, in URL) - The unique identifier of the project.
    Output:
    targetMetadata (object) - Contains schema.org metadata for target schema elements.
    Error Handling:
    404 Not Found if invalid projectId provided.
    500 Internal Server Error if error retrieving target metadata.
    
    '''
    try:
        # retrieve target metadata and return the status
        return {"status": "success", "message": "Target metadata retrieved successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

