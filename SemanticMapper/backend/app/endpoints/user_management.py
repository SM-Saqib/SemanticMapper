# 8.1 POST /api/v1/user/register
# Purpose: Register a new user and start a session.
# Input Parameters:
# Name
# Email
# Password
# Output:
# SessionToken (string)
# Status (string)
# Message (string)
# 8.2 POST /api/v1/user/login
# Purpose: Authenticate a user and start a session.
# Input Parameters:
# Email
# Password
# Output:
# SessionToken (string)
# Status (string)
# Message (string)
# 8.3.1 POST /api/v1/user/request-reset-password
# Purpose: Request a password reset.
# Input Parameters:
# Email
# Output:
# Status (string)
# Message (string)
# 8.3.2 POST /api/v1/user/confirm-reset-password
# Purpose: Confirm a password reset using a token sent to the user's email.
# Input Parameters:
# Token
# New Password
# Output:
# Status (string)
# Message (string)
# 8.4 DELETE /api/v1/user/{userId}
# Purpose: Delete a user account after confirmation.
# Input Parameters:
# UserId (string, in URL)
# Confirmation (boolean, in the body)
# Output:
# Status (string)
# Message (string)
# 8.5 POST /api/v1/user/logout
# Purpose: Log out a user and invalidate the session token.
# Input Parameters: SessionToken (string, in header)
# Output:
# Status (string)
# Message (string)
# 8.6 PUT /api/v1/user/{userId}
# Purpose: Update user information.
# Input Parameters:
# UserId (string, in URL)
# Updated information (in the body)
# Output:
# Status (string)
# Message (string)


from fastapi import APIRouter, HTTPException, Depends

router = APIRouter()

@router.post("/user/register", tags=["User Management APIs"])
async def register_user():
    '''
    Purpose: Register a new user and start a session.
    Input Parameters:
    Name
    Email
    Password
    Output:
    SessionToken (string)
    Status (string)
    Message (string)
    
    '''
    try:
        # register user and return the status
        return {"status": "success", "message": "User registered successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.post("/user/login", tags=["User Management APIs"])
async def login_user():
    '''
    Purpose: Authenticate a user and start a session.
    Input Parameters:
    Email
    Password
    Output:
    SessionToken (string)
    Status (string)
    Message (string)
    
    '''
    try:
        # login user and return the status
        return {"status": "success", "message": "User logged in successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.post("/user/request-reset-password", tags=["User Management APIs"])
async def request_reset_password():
    '''
    Purpose: Request a password reset.
    Input Parameters:
    Email
    Output:
    Status (string)
    Message (string)
    
    '''
    try:
        # request password reset and return the status
        return {"status": "success", "message": "Password reset requested successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.post("/user/confirm-reset-password", tags=["User Management APIs"])
async def confirm_reset_password():
    '''
    Purpose: Confirm a password reset using a token sent to the user's email.
    Input Parameters:
    Token
    New Password
    Output:
    Status (string)
    Message (string)
    
    '''
    try:
        # confirm password reset and return the status
        return {"status": "success", "message": "Password reset confirmed successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.delete("/user/{userId}", tags=["User Management APIs"])
async def delete_user(userId: str, confirmation: bool):
    '''
    Purpose: Delete a user account after confirmation.
    Input Parameters:
    UserId (string, in URL)
    Confirmation (boolean, in the body)
    Output:
    Status (string)
    Message (string)
    
    '''
    try:
        # delete user and return the status
        return {"status": "success", "message": "User deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    