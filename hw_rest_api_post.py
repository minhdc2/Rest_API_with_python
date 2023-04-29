import requests

BASE = 'http://127.0.0.1:5000/'
headers = {'accept': 'application/json'}
response = requests.post(BASE + 'example', headers=headers, json={'pool': [1,7,2,6,8], 'percentile': 99.5})
print(response.json())
#[1,7,2,6]
