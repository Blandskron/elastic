import requests
import json

url = "http://localhost:9200/my_index/_update/1"

payload = json.dumps({
  "doc": {
    "age": 31
  }
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
