import math
import pygame

# NOTE_NAMES = {
#     "C": 12,
#     "C♯": 13,
#     "D♭": 13,
#     "D": 14,
#     "D♯": 15,
#     "E♭": 15,
#     "E": 16,
#     "F": 17,
#     "F♯": 18,
#     "G♭": 18,
#     "G": 19,
#     "G♯": 20,
#     "A♭": 20,
#     "A": 21,
#     "A♯": 22,
#     "B♭": 22,
#     "B": 23,
# }
NOTE_NAMES = ['C','C♯','D','D♯','E','F','F♯','G','G♯','A','A♯','B']

def notes_to_freq(notes):
    BASE_FREQ = 440  # A4 = 440Hz
    freqs = []
    for note in notes:
        print(note)
        note_name = note[:-2]
        print(1)
        octave = int(note[-1])
        if len(note) == 4: # check for 2-digit octave
            octave = int(note[-2:])
        print(2)
        print(note_name)
        note_index = NOTE_NAMES.index(note_name)
        print(3)
        freq = BASE_FREQ * (2 ** ((note_index - 9) / 12)) * (2 ** octave)
        print(4)
        freqs.append(freq)
        print(freq)
    return freqs



# convert the notes in notes.txt into MIDI frequencies and store them in frequencies.txt
with open("notes.txt", "r", encoding='utf-8') as f:
    notes = f.read().split(" ")
    freqs = notes_to_freq(notes)
    with open("frequencies.txt", "w", encoding='utf-8') as f:
        for freq in freqs:
            f.write(str(freq) + " ")
