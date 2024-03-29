import crepe
import librosa
from librosa.core import midi_to_note
#import download
import subprocess
#import multiprocessing


if __name__ == "__main__":
    #multiprocessing.freeze_support()

    #subprocess.run('rm song/*', shell=True)
    #song = input('Enter a song:\n ')
    #url = download.search_spotify(song)
    #print(url)
    #download.download_song(url)

    file = subprocess.check_output('ls song | head -n 1', shell=True).decode().strip()



    #y, sr = librosa.load(f"song/{file}")
    y, sr = librosa.load(f"instrumental/song/accompaniment.wav")

    # Extract the pitch using the CREPE model
    time, frequency, confidence, activation = crepe.predict(y, sr, viterbi=True)
    

    # paste frequency into a text file
    with open("test_freq.txt", "w", encoding='utf-8') as f:
        for i in range(len(frequency)):
            f.write((f"{time[i]}: {frequency[i]}\n"))

    with open("times.txt", "w", encoding='utf-8') as f:
        for i in range(len(time)):
            f.write((f"{time[i]}\n"))
        

    with open("freq_only.txt", "w", encoding='utf-8') as f:
        for freq in frequency:
            f.write(str(freq) + " ")
    print("done!")

    # Convert pitches to notes
    #notes = [midi_to_note(frequency[i]) for i in range(len(frequency))]

    #print(notes)
    # with open("notes.txt", "w", encoding='utf-8') as f:
    #     for note in notes:
    #         f.write(note + " ")

