import mido

# Open the file and read in the note numbers
with open('frequencies.txt', 'r') as f:
    note_numbers = f.read().strip().split(' ')
note_numbers = [round(float(note_number)) for note_number in note_numbers]

# Create MIDI file and track
mid = mido.MidiFile()
track = mido.MidiTrack()
mid.tracks.append(track)

# Set tempo and time signature
tempo = mido.bpm2tempo(6000) # Assuming tempo of 98 BPM
track.append(mido.MetaMessage('set_tempo', tempo=tempo, time=0)) # Assuming tempo of 98 BPM
track.append(mido.MetaMessage('time_signature', numerator=3, denominator=4, clocks_per_click=24, notated_32nd_notes_per_beat=8, time=0))

# Convert each note number to MIDI note events
time = 0
for note_number in note_numbers:
    note_on = mido.Message('note_on', note=note_number, velocity=64, time=time)
    note_off = mido.Message('note_off', note=note_number, velocity=0, time=480) # Assuming quarter note duration
    track.append(note_on)
    track.append(note_off)
    time = 0

# Save MIDI file
mid.save('output.mid')