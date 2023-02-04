import requests, json, os
from requests.auth import HTTPBasicAuth

clientID = os.environ['CLIENT_ID']
clientSecret = os.environ['CLIENT_SECRET']

url = "https://accounts.spotify.com/api/token"
data = {"grant_type": "client_credentials"}
auth = HTTPBasicAuth(clientID, clientSecret)

response = requests.post(url, data=data, auth=auth)

#print(response.ok)
#print(response.json())
#print(response.status_code)

accessToken = response.json()["access_token"]

# ask user for an artist
artist = input("Artist: ".lower())
artist = artist.replace(" ", "%20")

url = "https://api.spotify.com/v1/search"
headers = {"Authorization": f"Bearer {accessToken}"}
search = f"?q={artist}%3Aqueen&type=track&limit=5"

fullURL = f"{url}{search}"
print(fullURL)

response = requests.get(fullURL, headers=headers)
data = response.json()

# print(json.dumps(data, indent=2))

for track in data["tracks"]["items"]:
  print(track["name"])
  print(track["preview_url"])
  print()
