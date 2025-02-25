from fastapi import FastAPI, HTTPException
from services.granite_service import query_granite
from database.db import save_to_db

app = FastAPI()

@app.post("/query")
async def handle_query(prompt: dict):
    """
    Endpoint to handle legal queries.
    - Receives a query from the frontend.
    - Sends it to IBM Granite for processing.
    - Saves the query and response in the database.
    - Returns the response to the frontend.
    """
    try:
        # Query IBM Granite
        response = query_granite(prompt["query"])

        # Save the query and response in the database
        save_to_db(prompt["query"], response)

        # Return the response to the frontend
        return {"response": response}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))