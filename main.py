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

        trackDetails = sp.audio_features(trackID)
        trackKey = trackDetails[0]["key"]
        trackLiveness = trackDetails[0]["liveness"]
        trackTimeSignature = trackDetails[0]["time_signature"]
        trackTempo = trackDetails[0]["tempo"]
        trackMode = trackDetails[0]["mode"]

        trackInfo.append(
            {
                "name": track,
                "key": trackKey,
                "liveness": trackLiveness,
                "time_signature": trackTimeSignature,
                "tempo": trackTempo,
                "mode": trackMode,
            })

    return trackInfo

print(getTrackKey(getTop10("pop")))