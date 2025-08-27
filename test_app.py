import requests

api_endpoint = "http://0.0.0.0:8080/chat"



payload = {
  "message": "Whats the status of the order with tracking ID T1234",
}
#"session_id": "string"


headers = {
    "accept": "application/json",
    "Content-Type": "application/json"
}

response = requests.post(api_endpoint, headers=headers, json=payload)
print(response.json())


