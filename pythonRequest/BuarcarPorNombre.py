import requests

url = "http://localhost:9200/my_index/_search"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
