import subprocess
import os
from pydub import AudioSegment
import dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spleeter.separator import Separator

# Using embedded configuration.
#separator = Separator('spleeter:2stems')


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
    convert_to_wav()
    # use spleeter to separate the vocals from the song
    # the audio file is saved as the only item in the song folder
    


def convert_to_wav():
    songName = os.listdir("song")[0]
    sound = AudioSegment.from_mp3("song/"+songName)
    sound.export('song/song.wav', format='wav')



def splitSong():
    # song_dir = 'song'
    # audioPath = os.path.join(song_dir, "song.wav")
    # separator = Separator('spleeter:2stems')
    # separator.separate_to_file(audioPath, destination='instrumental')
    convert_to_wav() 
    # run in a subprocess instead, works better to split song
    subprocess.run(f'spleeter separate -i song/song.wav -p spleeter:2stems -o instrumental', shell=True)
    print("Done!")

splitSong()

#convert_to_wav()