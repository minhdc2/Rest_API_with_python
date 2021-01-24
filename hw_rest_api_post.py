import requests

BASE = 'http://127.0.0.1:5000/'

response = requests.post(BASE + 'example', {'pool': [1,7,2,6], 'percentile': 99.5})
print(response.json())
#[1,7,2,6]
