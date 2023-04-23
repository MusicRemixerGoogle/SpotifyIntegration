import math
import numpy as np
NOTES = ["C", "C♯", "D", "D♯", "E", "F", "F♯", "G", "G♯", "A", "A♯", "B"]

def noteToMidi(note):
    """Convert a note to a MIDI number."""
    # Get the note name and octave
    
    note_name = note[0]
    # octave is everything after the note name
    # Check if the note is of the form C♯41
    if note[1] == "♯":
        if len(note) > 3:
            octave = int(note[-2:])
            note_name = note[:-2]
        else:
            octave = int(note[-1])
            note_name = note[:-1]
    else:
        octave = int(note[1:])

    # Get the index of the note name in the list of notes
    note_index = NOTES.index(note_name)

    # Calculate the MIDI number
    midi_number = (octave + 1) * 12 + note_index
    min_note = 0
    max_note = 127
    scaled_note = np.interp(midi_number, (min_note, max_note), (0, 127))

    int_note = int(scaled_note)

    return int_note

def freqToMidi(freq):
    """Convert a frequency to a MIDI number."""
    return 12 * (math.log2(freq / 440)) + 69 


# convert the notes in notes.txt into MIDI frequencies and store them in frequencies.txt
with open("freq_only.txt", "r", encoding='utf-8') as f:
    notes = f.read().strip().split(" ")
    with open("frequencies.txt", "w", encoding='utf-8') as f:
        counter = 0
        note_avg = 0
        for note in notes:
            try:
                note_avg += float(note)
                counter += 1
                if counter == 61:
                    f.write(str(freqToMidi(note_avg/counter)) + "\n")
                    counter = 0
                    note_avg = 0
            except Exception as e:
                print(e)
                print(note)
    with open("full_midi.txt", "w", encoding='utf-8') as f:
        for note in notes:
            f.write(str(freqToMidi(float(note))) + "\n")



print("done")