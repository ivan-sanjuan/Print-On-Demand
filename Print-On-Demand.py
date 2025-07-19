from auth import get_token
import requests

response_auth = get_token()
access_token = response_auth.json().get('access_token')
headers = {'Authorization': f'Bearer {access_token}', 'Accept': 'application/json'}
sand_url = 'https://api.sandbox.lulu.com/print-jobs-templates'

response_sand = requests.post(sand_url,headers=headers)

print(headers)