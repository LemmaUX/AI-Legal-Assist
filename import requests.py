import requests

# Endpoint de IBM Granite
url = "https://us-south.ml.cloud.ibm.com/ml/v1/text/generation?version=2023-05-29"

# Cuerpo de la solicitud
body = {
    "input": """<|start_of_role|>system<|end_of_role|>You are Granite, an AI language model developed by IBM in 2024. You are a cautious assistant. You carefully follow instructions. You are helpful and harmless and you follow ethical guidelines and promote positive behavior.<|end_of_text|>
<|start_of_role|>user<|end_of_role|>¿Qué es un contrato laboral?<|end_of_text|>
<|start_of_role|>assistant<|end_of_role|>""",
    "parameters": {
        "decoding_method": "greedy",
        "max_new_tokens": 900,
        "min_new_tokens": 0,
        "repetition_penalty": 1
    },
    "model_id": "ibm/granite-3-8b-instruct",
    "project_id": "6c9083c5-eac0-4e97-a87b-c51625c53d11",
    "moderations": {
        "hap": {
            "input": {
                "enabled": True,
                "threshold": 0.5,
                "mask": {
                    "remove_entity_value": True
                }
            },
            "output": {
                "enabled": True,
                "threshold": 0.5,
                "mask": {
                    "remove_entity_value": True
                }
            }
        },
        "pii": {
            "input": {
                "enabled": True,
                "threshold": 0.5,
                "mask": {
                    "remove_entity_value": True
                }
            },
            "output": {
                "enabled": True,
                "threshold": 0.5,
                "mask": {
                    "remove_entity_value": True
                }
            }
        }
    }
}

# Encabezados
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJraWQiOiIyMDI1MDEzMDA4NDQiLCJhbGciOiJSUzI1NiJ9.eyJpYW1faWQiOiJJQk1pZC02OTEwMDBNQ0dPIiwiaWQiOiJJQk1pZC02OTEwMDBNQ0dPIiwicmVhbG1pZCI6IklCTWlkIiwianRpIjoiMDM5NmJhMTgtZGU4NS00ODI4LTkwYzUtMDZhZjM3YzBhNjY3IiwiaWRlbnRpZmllciI6IjY5MTAwME1DR08iLCJnaXZlbl9uYW1lIjoiSm9yZ2UiLCJmYW1pbHlfbmFtZSI6IlRlcmNlcm9zIiwibmFtZSI6IkpvcmdlIFRlcmNlcm9zIiwiZW1haWwiOiJtZWdhbG9hdXRpc0BnbWFpbC5jb20iLCJzdWIiOiJtZWdhbG9hdXRpc0BnbWFpbC5jb20iLCJhdXRobiI6eyJzdWIiOiJtZWdhbG9hdXRpc0BnbWFpbC5jb20iLCJpYW1faWQiOiJJQk1pZC02OTEwMDBNQ0dPIiwibmFtZSI6IkpvcmdlIFRlcmNlcm9zIiwiZ2l2ZW5fbmFtZSI6IkpvcmdlIiwiZmFtaWx5X25hbWUiOiJUZXJjZXJvcyIsImVtYWlsIjoibWVnYWxvYXV0aXNAZ21haWwuY29tIn0sImFjY291bnQiOnsidmFsaWQiOnRydWUsImJzcyI6ImY2ZmQ2NWQ1Y2ViMjRkZTc5OTQ1OWIwOGU1ZDRiMGY1IiwiaW1zX3VzZXJfaWQiOiIxMzMwNjQwNiIsImZyb3plbiI6dHJ1ZSwiaW1zIjoiMjk3MTM0NiJ9LCJpYXQiOjE3NDAxNzcwOTMsImV4cCI6MTc0MDE4MDY5MywiaXNzIjoiaHR0cHM6Ly9pYW0uY2xvdWQuaWJtLmNvbS9pZGVudGl0eSIsImdyYW50X3R5cGUiOiJ1cm46aWJtOnBhcmFtczpvYXV0aDpncmFudC10eXBlOmFwaWtleSIsInNjb3BlIjoiaWJtIG9wZW5pZCIsImNsaWVudF9pZCI6ImRlZmF1bHQiLCJhY3IiOjEsImFtciI6WyJwd2QiXX0.P_u3mVmn-uDnnKbdJUPMWwpoNEocKyo7jCW2LAhQNgVUReHmksveLf53coB0Hf5hlSBdoFZ6f5F73H9rahWFzufjOluOxXrzGxKNT1IPCACfYXISEUFm4MRkqZedwS4WaHzmAHSryt1D5iSsQnaV10SOgX-LoXJKoFbl06NgjZiYDrkGrUlDXBfpBqW1i8qjPGaRGxZmfuedqHtetsS3nd-04He4Jix6h4K6ZU-zXNfSFtg8j0o_PTybDycAIHyxtwdZgo9lHT9eGFFUxg-3zq4IgTQIZV5ZKFzihGAFplkc0w0BlPQjkTjUyYltH5vGhy9VASxgGN7SLGKSkJ7O6A"  # Reemplaza con tu token real
}

# Enviar la solicitud
response = requests.post(
    url,
    headers=headers,
    json=body
)

# Verificar la respuesta
if response.status_code != 200:
    raise Exception("Non-200 response: " + str(response.text))

# Procesar la respuesta
data = response.json()
print("Respuesta del modelo:", data["results"][0]["generated_text"])