import requests
import json

url = "http://localhost:9200/my_index/_doc/2"

payload = json.dumps({
  "name": "Jane Smith",
  "age": 25,
  "email": "janesmith@example.com"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
