import requests

url = "http://localhost:9200/my_index"

payload = {}
headers = {}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
