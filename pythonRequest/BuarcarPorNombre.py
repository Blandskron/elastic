import requests
import json

url = "http://localhost:9200/my_index/_search/"

payload = json.dumps({
  "query": {
    "match": {
      "name": "bastian"
    }
  }
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
