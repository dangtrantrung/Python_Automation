# RealPython.com
import requests
from requests.exceptions import Timeout

response=requests.get('https://api.github.com')
print(response.json())
print(response.json()['current_user_url'])
print("status_code",response.status_code)

try:
    response=requests.get('https://api.github.com')
    if (response.status_code==200):
        print('response.content:',response.content)
        print('response.header:',response.headers)
        print('response.header.content-type:',response.headers['Content-Type'])

except print('error'):
    print('error',requests.exceptions.HTTPError.strerror)

# Use GitHub’s repository search API to look for popular Python repositories:
# Search GitHub's repositories for popular Python projects
response = requests.get(
    "https://api.github.com/search/repositories",
    params={"q": "language:python", "sort": "stars", "order": "desc"},
)

# Inspect some attributes of the first three repositories
json_response = response.json()
popular_repositories = json_response["items"]
print('popular_repositories count',len(popular_repositories))
for repo in popular_repositories[:3]:
    print("Top 3 Github repo by Python")
    print(f"Name: {repo['name']}")
    print(f"Description: {repo['description']}")
    print(f"Stars: {repo['stargazers_count']}")
    print()
print("popular_repositories_name",[repo['name'] for repo in popular_repositories])
print("Total_repositories_python",json_response['total_count'])

# repositories_javascript
response_js = requests.get(
    "https://api.github.com/search/repositories",
    params={"q": "language:javascript", "sort": "stars", "order": "desc"},
)
json_response1 = response_js.json()
print("Total_repositories_javascript",json_response1['total_count'])
diff=(json_response1['total_count']-json_response['total_count'])*100/json_response['total_count']
# get the diff
print(f'Github repos JS and python count= {diff:.2f}%')


# time out
# request establishes a connection within 3.05 seconds and receives data within 5 seconds of the connection being established,
try:
    response = requests.get("https://api.github.com", timeout=3.5)
except Timeout:
    print("The request timed out")
    print(TimeoutError.strerror)
else:
    print("The request did not time out")
