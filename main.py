from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth




date = input("Which year you want to travel to? Type the data in the format YYYY-MM-DD : ")
year = date[0:4]


response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
text = response.text

soup = BeautifulSoup(text, "html.parser")
songs = [song.getText().strip() for song in soup.find_all(name="h3", id="title-of-a-story")]

res = []
for i in songs:
    if i not in res:
        res.append(i)

list_of_songs = res[6:10]
print(list_of_songs)

CLIENT_ID = client_id
CLIENT_SECRET = client_secret



sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)


user_id = sp.current_user()["id"]

uri_list = []
for song in list_of_songs:
    try:
        search = sp.search(q=song, limit=1, offset=0, type='track', market="US")
        uri = search["tracks"]["items"][0]["uri"]
        id = search["tracks"]["items"][0]["id"]
        uri_list.append(uri)

        

    except:
        pass

playlist = sp.user_playlist_create(user_id, f"{date} Trending Songs", public=True, collaborative=False, description='')
sp.playlist_add_items(playlist_id=playlist["id"], items=uri_list)



















