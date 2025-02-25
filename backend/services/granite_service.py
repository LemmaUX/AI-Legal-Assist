import requests
import pinecone
from sentence_transformers import SentenceTransformer

# Configuration for IBM Granite
GRANITE_URL = "https://us-south.ml.cloud.ibm.com/ml/v1/text/generation?version=2023-05-29"
ACCESS_TOKEN = "Your Token access"
# Configuration for Pinecone
PINECONE_API_KEY = "key"  # Reemplaza con tu API Key de Pinecone
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
