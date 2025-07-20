import requests
from config import client_key, client_secret, token_url

def get_token():
    payload = {
        'grant_type': 'client_credentials',
        'client_id': client_key,
        'client_secret': client_secret
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }
    response = requests.post(token_url,data=payload,headers=headers)
    return response