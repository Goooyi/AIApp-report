# Here's a minimal functioning example of how to use the producthunt GraphQL API using python.
# make sure to insert your own Developer Token, which you can get in the here https://www.producthunt.com/v2/oauth/applications
# to access different data, you need to change the query below. you can test queries in the API explorer https://ph-graph-api-explorer.herokuapp.com/
# lots of further details on queries can be found here http://api-v2-docs.producthunt.com.s3-website-us-east-1.amazonaws.com/object/viewer/#user
import os
import json
import requests
import httpx

PH_API_KEY = os.environ.get("PH_API_KEY")
PH_API_SECRET = os.environ.get("PH_API_SECRET")
PH_DEV_TOKEN = os.environ.get("PH_DEV_TOKEN")

print(PH_API_KEY)
headers = {
'Accept': 'application/json',
'Content-Type': 'application/json',
'Authorization': 'Bearer _BRJX-2mPl3MVf5iPb1rWZGY6aKqZJTQAgWk0_T0ZIU',
'Host': 'api.producthunt.com'
}

# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}

def run_query(query): # A simple function to use requests.post to make the API call. Note the json= section.
    request = httpx.post('https://api.producthunt.com/v2/api/graphql', data=json.dumps(query), headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code {}.".format(request.status_code))


# The GraphQL query (with a few aditional bits included) itself defined as a multi-line string.
query ={
  "query": "query { posts(first: 1) { edges { node { id, name } } } }"
}

print(headers)
result = run_query(query) # Execute the query
print(result)