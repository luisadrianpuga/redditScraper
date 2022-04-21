
import requests
import json

# note that CLIENT_ID refers to 'personal use script' and SECRET_TOKEN to 'token'
auth = requests.auth.HTTPBasicAuth('', '')

# here we pass our login method (password), username, and password
data = {'grant_type': '',
        'username': '',
        'password': ''}

# setup our header info, which gives reddit a brief description of our app
headers = {'User-Agent': 'MyBot/0.0.1'}

# send our request for an OAuth token
res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)

# convert response to JSON and pull access_token value
TOKEN = res.json()['access_token']

# add authorization to our headers dictionary
headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}
params = {'limit': 100000000}
# while the token is valid (~2 hours) we just add headers=headers to our requests
requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)


res = requests.get("https://oauth.reddit.com//user/leanluis/saved",
                headers=headers, params=params)

print(res.json())  # let's see what we get
with open('data.txt', 'w') as f:
  json.dump(res.json(), f, ensure_ascii=False)
#for item in res.json ()['data' ]['children']:
 #   print(item['data']['title'])