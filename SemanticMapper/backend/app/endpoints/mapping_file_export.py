
from fastapi import APIRouter, HTTPException, Depends

router = APIRouter()

@router.get("/export/mapping/{projectId}", tags=["Export APIs"])
async def export_semantic_mapping(projectId: str):
    '''
    Purpose: Retrieve semantic mapping result for a specific project.
    Input Parameters:
    projectId (string, in URL) - The unique identifier of the project.
    format (string, optional) - The desired format for the exported file, such as JSON, XML, etc.
    Output: mappingResult (object or file) - The final semantic mapping, including the final state of the semantic mapping, the time the mapping was completed, the user who completed the mapping, and the results of any validation checks.
    Error Handling:
    404 Not Found if an invalid projectId is provided.
    500 Internal Server Error if there is a server-side error when retrieving the mapping result.

    '''
    try:
        # export semantic mapping and return the status
        return {"status": "success", "message": "Semantic mapping exported successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.get("/export/enrichments/{projectId}", tags=["Export APIs"])
async def export_enrichments(projectId: str):
    '''
    Purpose: Retrieve original schema enrichments for a specific project.
    Input Parameters: projectId (string, in URL) - The unique identifier of the project.
    Output: enrichments (object) - The original schema enrichments, including documentation, descriptions of the intended use of each schema element, examples of data values, and links to related resources.
    Error Handling:
    404 Not Found if an invalid projectId is provided.
    500 Internal Server Error if there is a server-side error when retrieving the enrichments.
    
    '''
    try:
        # export enrichments and return the status
        return {"status": "success", "message": "Enrichments exported successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

