import math
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

def getSingleTrack(trackName) -> list:

    trackList = []
    trackID = sp.search(trackName, type="track", limit=1)
    trackID = trackID["tracks"]["items"][0]["id"]

    trackDetails = sp.audio_features(trackID)
    trackKey = trackDetails[0]["key"]
    trackTimeSignature = trackDetails[0]["time_signature"]
    trackTempo = trackDetails[0]["tempo"]
    trackMode = trackDetails[0]["mode"]
    trackDanceability = trackDetails[0]["danceability"]

    trackInfo = {
        "name": trackName,
        "key": trackKey,
        "danceability": trackDanceability,
        "time_signature": trackTimeSignature,
        "tempo": trackTempo,
        "mode": trackMode,
    }

    trackList.append(trackInfo)
    return trackList


def getTracksInfo(trackNames) -> list:
    trackInfo = []
    for track in trackNames:
        trackID = sp.search(track, type="track", limit=1)
        trackID = trackID["tracks"]["items"][0]["id"]

        trackDetails = sp.audio_features(trackID)
        trackKey = trackDetails[0]["key"]
        trackTimeSignature = trackDetails[0]["time_signature"]
        trackTempo = trackDetails[0]["tempo"]
        trackMode = trackDetails[0]["mode"]
        trackDanceability = trackDetails[0]["danceability"]

        trackInfo.append(
            {
                "name": track,
                "key": trackKey,
                "danceability": trackDanceability,
                "time_signature": trackTimeSignature,
                "tempo": trackTempo,
                "mode": trackMode,
            })

    return trackInfo


#pop = getTracksInfo(getTop10("pop"))
#print(pop)

def getAvgDanceability(trackInfo) -> int:
    total = 0
    for track in trackInfo:
        total += track["danceability"] * 10 # danceability btwn 0 and 1, so we multiply by 10 to get a whole number
    return total / len(trackInfo)


def getAvgKey(trackInfo) -> int:
    total = 0
    for track in trackInfo:
        total += track["key"]
    if getAvgDanceability(trackInfo) >= 5 : # we want to round up if the average danceability is greater than 5
        return math.ceil(total / len(trackInfo))
    return total // len(trackInfo)


def getAvgTempo(trackInfo) -> int:
    total = 0
    for track in trackInfo:
        total += track["tempo"]
    if getAvgDanceability(trackInfo) >= 5 : # we want to round up if the average danceability is greater than 5
        return math.ceil(total / len(trackInfo))
    return total // len(trackInfo)

def getAvgTimeSignature(trackInfo) -> int:
    total = 0
    for track in trackInfo:
        total += track["time_signature"]
    if getAvgDanceability(trackInfo) >= 5 : # we want to round up if the average danceability is greater than 5
        return math.ceil(total / len(trackInfo))
    return total // len(trackInfo)

# slowDancingInTheDark = getSingleTrack("Slow Dancing in the Dark")
# rivers = getSingleTrack("Rivers in the Desert")
# #print(slowDancingInTheDark)
# print (getAvgKey(pop))
# print (getAvgKey(rivers))

happyBirthday = getSingleTrack("Happy Birthday to You -- Happy Birthday TA")
print (getAvgKey(happyBirthday))
print (getAvgTempo(happyBirthday))
print (getAvgTimeSignature(happyBirthday))
print (getAvgDanceability(happyBirthday))
