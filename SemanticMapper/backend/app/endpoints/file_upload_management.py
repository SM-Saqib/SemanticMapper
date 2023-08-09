#./backend/app/endpoints/file_upload_management.py
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer

#import File from fastapi
from fastapi import File

router = APIRouter()

@router.post("/schemas/{projectId}", )
async def upload_schema_file(projectId: str, schemaFile: bytes = File(...)):
    try:
        # upload the schema file and return the status
        return {"status": "success", "message": "Schema file uploaded successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.post("/metadata/{projectId}", )
async def upload_metadata_file(projectId: str, metadataFile: bytes = File(...)):
    try:
        # upload the metadata file and return the status
        return {"status": "success", "message": "Metadata file uploaded successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.get("/schemas/status/{projectId}", )
async def get_schema_upload_status(projectId: str):
    try:
        # get the schema upload status and return the status
        return {"status": "uploaded", "message": "Schema file uploaded successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/project/save/{projectId}", )
async def save_project_state(projectId: str, projectState: dict):
    try:
        # save the project state and return the status
        return {"status": "success", "message": "Project state saved successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/project/load/{projectId}", )
async def load_project_state(projectId: str):
    try:
        # load the project state and return the status
        return {"status": "success", "message": "Project state loaded successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/project/load/{projectId}", )
async def load_project_state(projectId: str):
    try:
        # load the project state and return the status
        return {"status": "success", "message": "Project state loaded successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

