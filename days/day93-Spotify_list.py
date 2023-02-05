# build a Flask app
# form that has a year selector and a "Go" button
# query that constructs a list that outputs 10 songs from that year and a sample audio for each
# use:
#<audio controls>
#  <source src="<insert link to spotify here>" type="audio/mpeg">
#</audio>
# extra marks for adding a track offset that resets after 200 tracks

from flask import Flask, redirect, request
import requests, json, os
from requests.auth import HTTPBasicAuth
from replit import db


def songList(year):
  # auth on spotify
  clientID = os.environ['CLIENT_ID']
  clientSecret = os.environ['CLIENT_SECRET']

  # main url
  url = "https://accounts.spotify.com/api/token"
  # connection type and auth based on client ID and secret
  data = {"grant_type": "client_credentials"}
  auth = HTTPBasicAuth(clientID, clientSecret)

  # post the resquest using the above credentials
  # save the response in a variable
  response = requests.post(url, data=data, auth=auth)

  # print connection result and get access token
  #print(f'{response.ok}\n{response.json()}\n{response.status_code}')

  #access token
  accessToken = response.json()["access_token"]

  # form the search for spotify
  # auth for the search
  headers = {"Authorization": f"Bearer {accessToken}"}

  # offset to loop through the first 200 songs in the response
  offset = 0
  try:
    offset = db[year]
    if db[year] > 200:
      db[year] = 0
    db[year] += 10
  except:
    db[year] = 10

  # url and search
  url = "https://api.spotify.com/v1/search"
  search = f"?q={year}%3A1980&type=track&limit=10&offset={offset}"
  fullURL = f"{url}{search}"
  print(fullURL)

  response = requests.get(fullURL, headers=headers)
  data = response.json()

  # print to test out the request works
  #print(json.dumps(data, indent=2))

  # used this to print the tracks first
  #  for track in data["tracks"]["items"]:
  #    print(f"{track['name']} - {track['artists'][0]['name']}")
  #    print(track['preview_url'])
  #    print()

  songs = ''
  f = open('song.html', 'r')
  songs = f.read()
  f.close()

  song_list = ""

  # loop through the songs, output their name and preview_url
  # add the songs to the song_list and display song_list
  for track in data["tracks"]["items"]:
    thisTrack = songs
    thisTrack = thisTrack.replace(
      "{name}", f"""{track["name"]} - {track['artists'][0]['name']}""")
    thisTrack = thisTrack.replace("{url}", track['preview_url'])
    song_list += thisTrack

  return song_list


# build the app
app = Flask(__name__)


@app.route('/', methods=["POST"])
def songs():
  page = ''
  f = open('index.html', 'r')
  page = f.read()
  f.close()
  year = request.form["year"]
  songs = songList(year)
  page = page.replace("{content}", songs)
  page = page.replace("{year}", year)
  return page


@app.route('/')
def index():
  #form = request.form
  page = ''
  f = open('index.html', 'r')
  page = f.read()
  f.close()

  page = page.replace("{content}", "")
  page = page.replace("{year}", "1986")
  return page


app.run(host='0.0.0.0', port=81)

# files
# index.html
#<!DOCTYPE html>
#<html lang="en">
#  <head>
#    <meta charset="UTF-8">
#    <meta name="viewport" content="width=device-width, initial-scale=1.0">
#    <meta http-equiv="X-UA-Compatible" content="ie=edge">
#    <title>Songs</title>
#    <!-- <link rel="stylesheet" href="style.css"> -->
#  </head>
#  <body>
#    <h2>Tracks through time</h2>
#    <form method="post" action='/'>
#      <label for="year">Year: </label>
#      <input name="year" type="number" min="1960" max="2023" step="1" value="{year}" />
#      <button type="submit">Go</button>
#    </form>
#    <hr>
#    {content}
#  </body>
#</html>

# song.html
#<h2>{name}</h2>
#<br>
#<audio controls>
#  <source src="{url}" type="audio/mpeg">
#</audio>
#<hr>
