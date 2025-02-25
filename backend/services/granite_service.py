import requests
import pinecone
from sentence_transformers import SentenceTransformer

# Configuration for IBM Granite
GRANITE_URL = "https://us-south.ml.cloud.ibm.com/ml/v1/text/generation?version=2023-05-29"
ACCESS_TOKEN = "eyJraWQiOiIyMDI1MDEzMDA4NDQiLCJhbGciOiJSUzI1NiJ9.eyJpYW1faWQiOiJJQk1pZC02OTEwMDBNQ0dPIiwiaWQiOiJJQk1pZC02OTEwMDBNQ0dPIiwicmVhbG1pZCI6IklCTWlkIiwianRpIjoiOTUzNTczN2YtNGFiNS00N2M2LTljZGEtMDE3NjM1MzZmNzJkIiwiaWRlbnRpZmllciI6IjY5MTAwME1DR08iLCJnaXZlbl9uYW1lIjoiSm9yZ2UiLCJmYW1pbHlfbmFtZSI6IlRlcmNlcm9zIiwibmFtZSI6IkpvcmdlIFRlcmNlcm9zIiwiZW1haWwiOiJtZWdhbG9hdXRpc0BnbWFpbC5jb20iLCJzdWIiOiJtZWdhbG9hdXRpc0BnbWFpbC5jb20iLCJhdXRobiI6eyJzdWIiOiJtZWdhbG9hdXRpc0BnbWFpbC5jb20iLCJpYW1faWQiOiJJQk1pZC02OTEwMDBNQ0dPIiwibmFtZSI6IkpvcmdlIFRlcmNlcm9zIiwiZ2l2ZW5fbmFtZSI6IkpvcmdlIiwiZmFtaWx5X25hbWUiOiJUZXJjZXJvcyIsImVtYWlsIjoibWVnYWxvYXV0aXNAZ21haWwuY29tIn0sImFjY291bnQiOnsidmFsaWQiOnRydWUsImJzcyI6ImY2ZmQ2NWQ1Y2ViMjRkZTc5OTQ1OWIwOGU1ZDRiMGY1IiwiaW1zX3VzZXJfaWQiOiIxMzMwNjQwNiIsImZyb3plbiI6dHJ1ZSwiaW1zIjoiMjk3MTM0NiJ9LCJpYXQiOjE3NDAyOTg2NDUsImV4cCI6MTc0MDMwMjI0NSwiaXNzIjoiaHR0cHM6Ly9pYW0uY2xvdWQuaWJtLmNvbS9pZGVudGl0eSIsImdyYW50X3R5cGUiOiJ1cm46aWJtOnBhcmFtczpvYXV0aDpncmFudC10eXBlOmFwaWtleSIsInNjb3BlIjoiaWJtIG9wZW5pZCIsImNsaWVudF9pZCI6ImRlZmF1bHQiLCJhY3IiOjEsImFtciI6WyJwd2QiXX0.Nb1nLAcy6_wdFVq-u4TDmyP4Wd4exDFug8wjSWRgdJ8uN0muBdIz8vOOJdimCY8awjSwoQqgZ-wzP6zYoKjlHDVxGZ6i1Smwzt-q5y_tumgMwueOxYF4BAwv_miHiMRBpsimmqwfdA7e3-_LR8XuGvnBdoDsCq2eFD_UwL-3V9MdzZPSNteTaW5TTdqUMu--sF1QgkxUothEwS8fjZiiY21iinVR4jt60Xw5OtCLFuHNS20PEd8T3KSmnNgDAv58w7GUzPD75HFYLgLQdt3j08YB3KL2pLP-e1ufcK8JeJBoEDGEhh89LrGQcQL3HExqMkYXnqfSAuQk1qwyZVSrGA"  # Reemplaza con tu token real

# Configuration for Pinecone
PINECONE_API_KEY = "pcsk_5qFVzp_8yKxBAB3JBrkJpxuWta1zV5xXG13M4omz8Sfn9JXa9ad4RKFfBN5R5Cuo2mAuzK"  # Reemplaza con tu API Key de Pinecone
PINECONE_ENVIRONMENT = "us-west1-gcp"  # Reemplaza con tu región de Pinecone
PINECONE_INDEX_NAME = "legal-documents"  # Nombre del índice en Pinecone

# Initialize Pinecone
pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENVIRONMENT)
index = pinecone.Index(PINECONE_INDEX_NAME)

# Load the embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

def query_granite(prompt: str) -> str:
    """
    Sends a query to IBM Granite and returns the generated response.
    Includes semantic search with Pinecone for relevant documents.
    """
    try:
        # Step 1: Generate embedding for the query
        query_embedding = model.encode(prompt).tolist()

        # Step 2: Search Pinecone for relevant documents
        results = index.query(queries=[query_embedding], top_k=3)  # Retrieve top 3 relevant documents
        relevant_docs = " ".join([match['id'] for match in results['matches']])  # Extract document IDs or text

        # Step 3: Construct the full prompt with retrieved documents
        full_prompt = f"""<|start_of_role|>system<|end_of_role|>You are an AI legal assistant.<|end_of_text|>
                          <|start_of_role|>user<|end_of_role|>{prompt}<|end_of_text|>
                          Relevant Documents: {relevant_docs}
                          <|start_of_role|>assistant<|end_of_role|>"""

        # Step 4: Query IBM Granite
        body = {
            "input": full_prompt,
            "parameters": {
                "decoding_method": "greedy",
                "max_new_tokens": 900,
                "min_new_tokens": 0,
                "repetition_penalty": 1
            },
            "model_id": "ibm/granite-3-8b-instruct",
            "project_id": "6c9083c5-eac0-4e97-a87b-c51625c53d11"
        }

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {ACCESS_TOKEN}"
        }

        # Send the request to IBM Granite
        response = requests.post(GRANITE_URL, headers=headers, json=body)

        if response.status_code != 200:
            raise Exception("Error querying IBM Granite")

        # Process the response
        data = response.json()
        return data["results"][0]["generated_text"]

    except Exception as e:
        print(f"Error: {e}")
        return "An error occurred while processing your request."