from flask import Flask
from config import DevConfig

import requests
import spotipy
import spotipy.oauth2 as oauth2
import csv


app = Flask(__name__)

userid = '11158258963'

username = 'username' #placeholder value here
client_id = 'da0f87b9a7cf427795752f99600f40e9' #placeholder value here
client_secret = '1e9df059dc0943a29ed2143626c92df2' #placeholder value here
redirect_uri = 'http://localhost:5000/callback/'
scope = 'playlist-read-private'

# import spotipy.util as util
# token = util.prompt_for_user_token(
#         username=username,
#         scope=scope,
#         client_id=client_id,
#         client_secret=client_secret,
#         redirect_uri=redirect_uri)

# spotify = spotipy.Spotify(auth=token)

# credentials = oauth2.SpotifyClientCredentials(
#         client_id=client_id,
#         client_secret=client_secret)

# token = credentials.get_access_token()
# spotify = spotipy.Spotify(auth=token)

# playlists = spotify.current_user_saved_tracks()
# playlists = spotify.user_playlist(username)


url  = "https://api.spotify.com/v1/me/playlists"
headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer BQC7QdnNipgo_PFiov5w_Cl2AOZmKYSCxH5Ec_KQvdw3-1NEzytG5oeTGWqO8ywGBnNbU9GNGmnGjjGkKKJsoICsY_5bacuPgxr5SYzbXm_MY02WxUoefIvJWhgMUROD5-XgkBcLlSLhqbqvOI-ogk2gNqvS4fUAi9K1Xcg'
}
response = requests.get(url, headers=headers)
playlist_item = response.json()
# print(playlist_item)
# print(type(response))
# print(type(playlist_item["items"]))
playlisturl = []
for i in playlist_item["items"]:
    # print(i["id"], i["name"], i["tracks"])
    playlisturl.append(i["tracks"]["href"])

trackids = []
for listurl in playlisturl:
    url  = listurl
    headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer BQC7QdnNipgo_PFiov5w_Cl2AOZmKYSCxH5Ec_KQvdw3-1NEzytG5oeTGWqO8ywGBnNbU9GNGmnGjjGkKKJsoICsY_5bacuPgxr5SYzbXm_MY02WxUoefIvJWhgMUROD5-XgkBcLlSLhqbqvOI-ogk2gNqvS4fUAi9K1Xcg'
    }
    response = requests.get(url, headers=headers)
    tracks_item = response.json()
    for i in tracks_item["items"]:
        # print(i['track']["id"], i['track']["name"], i['track']['href'])
        trackids.append(i['track']['id'])

allUserTracksinPlaylists = []
for trackid in trackids:
    url  = 'https://api.spotify.com/v1/audio-features/{}'.format(trackid)
    # print(url)
    headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer BQC7QdnNipgo_PFiov5w_Cl2AOZmKYSCxH5Ec_KQvdw3-1NEzytG5oeTGWqO8ywGBnNbU9GNGmnGjjGkKKJsoICsY_5bacuPgxr5SYzbXm_MY02WxUoefIvJWhgMUROD5-XgkBcLlSLhqbqvOI-ogk2gNqvS4fUAi9K1Xcg'
            }
    response = requests.get(url, headers=headers)
    tracks_features = response.json()
    # print(tracks_features)
    allUserTracksinPlaylists.append(tracks_features)

print(allUserTracksinPlaylists[0])
print(len(allUserTracksinPlaylists))

###### put into cluster model ######

# return a vector (user score)


####### web #########
# @app.route("/")
# def hello():
#     return "Hello World!" + response.text

# if __name__ == "__main__":
#     app.run(debug=True)


