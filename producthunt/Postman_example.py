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
  'Cookie': '_producthunt_session_production=8grO1NQtYeFQ%2Fn4DOo%2FwNQrsX%2B9xC61cOCwdyzDjeW6rEBZ3EJjlTxKXTwKVvSoYF8q2wRQcZcvizMG4cX5jUpPVshQpISBKQnKQYsikd1oy3OHNb2C6uMJS5esUvGPQfeHxNft9ysE%2B9kvRdVA%2FVS59yJYOJYqCSfv4rd%2BnyxvztJGmZkc041YIFtX%2B1hNxZQNjlOBctFmJrdnTeEiLoi802bcRYbDLnmP5oI131MXGd6Ih4Pgi8vO%2FlBp5UmsaarzwCKltc5woUdy0QKizDQoQLieuGBnp6OA%2BB6xIIhDaH60Yp%2B5ZZ9HXbyaS9kHvRhMCnEPAirFaDlzIc9OtEzxtTSjmO8YZ8nHCfKTVeeO6t3k%2B5YiRvTMj736pJXDbRiafnn8Knr17Rdz0wEePw8mYGjrZMfpdm5m7gozZ6rkwvqWgUe7H%2BwSpv94r--XfcxxV8BXG458BfB--hqxHi5JtS2yj9sSfNruqzg%3D%3D; csrf_token=AafAgkdZOQvx6BUh5iBXD9i41pRr9CjhC_kxQzTYEv56bLasRoZO-oNbBA8MDncCeTsYxsHuJIPWvg4I2tvTFA; track_code=c4d54d0c96; visitor_id=4dff8b27-3749-4f74-a145-fea8e819e0d2'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
print(response.status_code)
