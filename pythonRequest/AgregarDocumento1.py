import requests
import json

url = "http://localhost:9200/my_index/_doc/1"

payload = json.dumps({
  "name": "John Doe",
  "age": 30,
  "email": "johndoe@example.com"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
