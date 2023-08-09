# the main function that will run the app

# backend/main.py
from fastapi import FastAPI
from app.api import api_router  # Import the API router from app.api

app = FastAPI()

# Include the router for your APIs
app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn

    # Run the FastAPI application locally with Uvicorn on localhost port 5000
    uvicorn.run("main:app", host="localhost", port=5000, reload=True)
