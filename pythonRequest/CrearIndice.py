import requests
import json

url = "http://localhost:9200/my_index"

payload = json.dumps({
  "settings": {
    "number_of_shards": 1,
    "number_of_replicas": 1
  }
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
