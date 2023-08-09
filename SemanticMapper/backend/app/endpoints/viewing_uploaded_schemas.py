

from fastapi import APIRouter, HTTPException, Depends

router = APIRouter()

@router.get("/schemas/{projectId}", tags=["Schema APIs"])
async def get_schemas(projectId: str):
    '''
    Purpose: Retrieve list of all uploaded schemas for a specific project.
    Input Parameters:
    projectId (string, in URL) - The unique identifier of the project.
    Output:
    schemas (array of objects) - List of schema objects containing name, file path, date uploaded etc.
    Error Handling:
    404 Not Found if invalid projectId provided.
    500 Internal Server Error if error retrieving schemas.
    
    '''
    try:
        # retrieve schemas and return the status
        return {"status": "success", "message": "Schemas retrieved successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

