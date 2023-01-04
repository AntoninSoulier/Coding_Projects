import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials

Client_ID = "c05331a05d7c4ea3aa8b3e6f938e9e16"
Client_Secret = "aab89dc900c44d97b5950f6634656762"

client_credentials_manager = SpotifyClientCredentials(client_id=Client_ID, client_secret=Client_Secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

artist_name = []
track_name = []
popularity = []
track_id = []

for i in range(0,1000,50):
    track_results = sp.search(q='year:2021', type='track', limit=50,offset=i)
    for i, t in enumerate(track_results['tracks']['items']):
        artist_name.append(t['artists'][0]['name'])
        track_name.append(t['name'])
        track_id.append(t['id'])
        popularity.append(t['popularity'])

track_dataframe = pd.DataFrame({'artist_name': artist_name,'track_name':track_name,'track_id':track_id,'popularity':popularity})

#print(track_dataframe.shape)
print(track_dataframe)

track_id = "65OVbaJR5O1RmwOQx0875b"
track_data = sp.track(track_id)
streams = track_data['popularity']
