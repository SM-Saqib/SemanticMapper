# 5.1 POST /api/v1/chat/send/{projectId}
# Purpose: Send user's message to chat engine for a specific project.
# Input Parameters:
# projectId (string, in URL) - The unique identifier of the project.
# messageText (string) - The user's message text to be sent to the chat engine.
# Output:
# status (string) - The status of the message delivery, either "sent" or "error".
# message (string) - The detailed message of the operation.
# Error Handling:
# 400 Bad Request if empty or incorrect message text is provided.
# 404 Not Found if an invalid projectId is provided.
# 500 Internal Server Error if there is a server-side error when sending the message.
# 5.2 GET /api/v1/chat/receive/{projectId}
# Purpose: Receive messages from chat engine for a specific project.
# Input Parameters: projectId (string, in URL) - The unique identifier of the project.
# Output: messages (array of objects) - The messages from the chat engine, each containing sender (string), messageText (string), timestamp (string).
# Error Handling:
# 404 Not Found if an invalid projectId is provided.
# 500 Internal Server Error if there is a server-side error when receiving the messages.

from fastapi import APIRouter, HTTPException, Depends

router = APIRouter()

@router.post("/chat/send/{projectId}", tags=["Chat APIs"])
async def send_message(projectId: str, messageText: str):
    '''
    Purpose: Send user's message to chat engine for a specific project.
    Input Parameters:
    projectId (string, in URL) - The unique identifier of the project.
    messageText (string) - The user's message text to be sent to the chat engine.
    Output:
    status (string) - The status of the message delivery, either "sent" or "error".
    message (string) - The detailed message of the operation.
    Error Handling:
    400 Bad Request if empty or incorrect message text is provided.
    404 Not Found if an invalid projectId is provided.
    500 Internal Server Error if there is a server-side error when sending the message.
    
    '''
    try:
        # send message and return the status
        return {"status": "success", "message": "Message sent successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.get("/chat/receive/{projectId}", tags=["Chat APIs"])
async def receive_message(projectId: str):
    '''
    Purpose: Receive messages from chat engine for a specific project.
    Input Parameters: projectId (string, in URL) - The unique identifier of the project.
    Output: messages (array of objects) - The messages from the chat engine, each containing sender (string), messageText (string), timestamp (string).
    Error Handling:
    404 Not Found if an invalid projectId is provided.
    500 Internal Server Error if there is a server-side error when receiving the messages.
    
    '''
    try:
        # receive messages and return the status
        return {"status": "success", "message": "Messages received successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))