import requests
from bs4 import BeautifulSoup
import spotipy
import credentials
from spotipy.oauth2 import SpotifyOAuth

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(f"https://billboard.com/charts/hot-100/{date}/")
response.raise_for_status()
soup = BeautifulSoup(response.text, 'html.parser')

all_titles = soup.find_all(name="h3", class_="a-no-trucate")

titles = [title.getText().strip() for title in all_titles]
#print(titles)

#feed your credential eg-> YOUR_APP_CLIENT_ID= "XXXXXXXXXXXXXX"

YOUR_APP_CLIENT_ID = credentials.YOUR_APP_CLIENT_ID
YOUR_APP_CLIENT_SECRET = credentials.YOUR_APP_CLIENT_SECRET
YOUR_APP_REDIRECT_URI = credentials.YOUR_APP_REDIRECT_URI

#now creating playlist in spotify

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=YOUR_APP_CLIENT_ID,
client_secret=YOUR_APP_CLIENT_SECRET,
redirect_uri=YOUR_APP_REDIRECT_URI,
scope="playlist-modify-private",
))

results = sp.current_user()
USER_ID = results['id']
#print(f"USER_ID is {USER_ID}")

uris = [sp.search(title)['tracks']['items'][0]['uri'] for title in titles]

PLAYLIST_ID = sp.user_playlist_create(user=USER_ID,public=False,name=f"{date} BillBoard-100")['id']

sp.user_playlist_add_tracks(playlist_id=PLAYLIST_ID,tracks=uris,user=USER_ID)