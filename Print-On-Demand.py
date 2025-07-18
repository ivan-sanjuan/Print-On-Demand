from auth import get_token
import requests

response = get_token()
access_token = response.json().get('access_token')
headers = {'Authorization': f'Bearer {access_token}', 'Accept': 'application/json'}
prod_url = 'https://api.sandbox.lulu.com/print-jobs-templates'

response = requests.post(prod_url,headers=headers)

print("Status:", response.status_code)
print("Content-Type:", response.headers.get('Content-Type'))
print("Raw text:", response.text[:300])