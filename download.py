import subprocess
import os
from pydub import AudioSegment
import dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

dotenv.load_dotenv()
clientSecret = os.getenv("CLIENT_SECRET")
clientID = os.getenv("CLIENT_ID")

def search_spotify(query):
    client_credentials_manager = SpotifyClientCredentials(client_id=clientID, client_secret=clientSecret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    result = sp.search(query, type='track', limit=1)
    track_id = result['tracks']['items'][0]['id']
    url = f'https://open.spotify.com/track/{track_id}'
    return url



def download_song(url):
    subprocess.run(f'spotdl --output song --format mp3 {url}', shell=True)
    # get current path 
    # path = os.getcwd()
    # filename = subprocess.check_output(['spotdl',"--save-file", path , url]).decode().strip()
    # os.rename(filename, 'song.mp3')

def convert_to_wav():
    sound = AudioSegment.from_mp3('song.mp3')
    sound.export('song.wav', format='wav')

#convert_to_wav()