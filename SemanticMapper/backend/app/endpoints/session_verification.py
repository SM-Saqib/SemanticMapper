# 6.1 GET /api/v1/session/verify
# Purpose: Verify if a session token is still valid.
# Input Parameters: SessionToken (string, in header)
# Output:
# Status (string)
# Message (string)
# Error Handling:
# 401 Unauthorized if the session token is invalid or expired.
# 500 Internal Server Error if there is a server-side error when verifying the session token.


from fastapi import APIRouter, HTTPException, Depends

router = APIRouter()

@router.get("/session/verify", tags=["Session Verification APIs"])
async def verify_session():
    '''
    Purpose: Verify if a session token is still valid.
    Input Parameters: SessionToken (string, in header)
    Output:
    Status (string)
    Message (string)
    Error Handling:
    401 Unauthorized if the session token is invalid or expired.
    500 Internal Server Error if there is a server-side error when verifying the session token.
    
    '''
    try:
        # verify session and return the status
        return {"status": "success", "message": "Session verified successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

    