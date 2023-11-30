# Here's a minimal functioning example of how to use the producthunt GraphQL API using python.
# make sure to insert your own Developer Token, which you can get in the here https://www.producthunt.com/v2/oauth/applications
# to access different data, you need to change the query below. you can test queries in the API explorer https://ph-graph-api-explorer.herokuapp.com/
# lots of further details on queries can be found here http://api-v2-docs.producthunt.com.s3-website-us-east-1.amazonaws.com/object/viewer/#user
import os
import json
import requests

PH_API_KEY = os.environ.get("PH_API_KEY")
PH_API_SECRET = os.environ.get("PH_API_SECRET")
PH_DEV_TOKEN = os.environ.get("PH_DEV_TOKEN")

print(PH_API_KEY)
headers = {
'Accept': 'application/json',
'Content-Type': 'application/json',
'Authorization': 'Bearer ' + PH_DEV_TOKEN,
'Host': 'api.producthunt.com'
}

def run_query(query): # A simple function to use requests.post to make the API call. Note the json= section.
    request = requests.post('https://api.producthunt.com/v2/api/graphql', data=json.dumps(query), headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))


# The GraphQL query (with a few aditional bits included) itself defined as a multi-line string.
query = {"query":
        """
        query todayPosts {
            posts {
                totalCount
                edges {
                    node {
                        id
                        name
                        tagline
                        votesCount
                        featuredAt
                        makers {
                            name
                            followers {
                                totalCount
                            }
                            following {
                                totalCount
                            }
                            madePosts {
                                totalCount
                            }
                            twitterUsername
                        }
                    }
                }
            }
        }
        """}
result = run_query(query) # Execute the query
print(result)