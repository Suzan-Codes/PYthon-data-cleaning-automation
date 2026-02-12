# api_client.py
import requests
from config import API_URL, API_KEY

def send_to_api(data):
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    # sample POST request
    response = requests.post(API_URL, json=data, headers=headers)

    print("API request sent (sample)")
    return response.status_code
