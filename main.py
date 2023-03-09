import requests
import dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

dotenv.load_dotenv()
clientSecret = os.getenv("CLIENT_SECRET")
clientID = os.getenv("CLIENT_ID")

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=clientID, client_secret=clientSecret))


def getTop10(genre) -> list:
    playlist = sp.search(f"{genre} rising", type="playlist", limit=1)
    x = (playlist["playlists"]["items"][0])
    print(x["name"])
    playlistID = playlist["playlists"]["items"][0]["id"]
    playlistTracks = sp.playlist_tracks(playlistID, limit=10)
    tracks = playlistTracks["items"]
    # return an array of tracks
    tracks = [track["track"]["name"] for track in tracks]
    return tracks


def getTrackKey(trackNames) -> list:
    trackInfo = []
    for track in trackNames:
        trackID = sp.search(track, type="track", limit=1)
        trackID = trackID["tracks"]["items"][0]["id"]

        trackKey = sp.audio_features(trackID)
        trackKey = trackKey[0]["key"]
        trackLiveness = trackKey[0]["liveness"]
        trackTimeSignature = trackKey[0]["time_signature"]
        trackTempo = trackKey[0]["tempo"]
        trackMode = trackKey[0]["mode"]

        trackInfo.append(
            {
                "key": trackKey,
                "liveness": trackLiveness,
                "time_signature": trackTimeSignature,
                "tempo": trackTempo,
                "mode": trackMode,
            })

    return trackKeys

print(getTrackKey(getTop10("pop")))