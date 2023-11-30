import requests
import json

url = "https://api.producthunt.com/v2/api/graphql"

payload = json.dumps({
  "query": "query { posts(first: 1) { edges { node { id, name } } } }"
})
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer _BRJX-2mPl3MVf5iPb1rWZGY6aKqZJTQAgWk0_T0ZIU',
  'Host': 'api.producthunt.com',
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
print(response.status_code)
