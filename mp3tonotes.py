import crepe
import librosa
from librosa.core import midi_to_note
import download
import subprocess

subprocess.run('rm song/*', shell=True)
song = input('Enter a song:\n ')
url = download.search_spotify(song)
print(url)
download.download_song(url)

file = subprocess.check_output('ls song | head -n 1', shell=True).decode().strip()



y, sr = librosa.load(f"song/{file}")

# Extract the pitch using the CREPE model
time, frequency, confidence, activation = crepe.predict(y, sr, viterbi=True)

# Convert pitches to notes
notes = [midi_to_note(frequency[i]) for i in range(len(frequency))]

print(notes)
with open("notes.txt", "w", encoding='utf-8') as f:
    for note in notes:
        f.write(note + " ")