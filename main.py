import mido

# List of MIDI note numbers from frequencies.txt
notes = []
with open('frequencies.txt', 'r') as f:
    notes = f.read().split(' ')

# convert the notes to integers
notes = [int(note) for note in notes]
print(notes)

tempo = 98
time_signature = (3, 4)

# Create a new MIDI file
mid = mido.MidiFile()

# Add a new track to the MIDI file
track = mido.MidiTrack()
mid.tracks.append(track)

# Set the tempo (optional)
tempo = mido.bpm2tempo(tempo)
track.append(mido.MetaMessage('set_tempo', tempo=tempo))

# Set the time signature (optional)
time_signature = mido.MetaMessage('time_signature', numerator=3, denominator=4)
track.append(time_signature)

# Set the key signature (optional)
key_signature = mido.MetaMessage('key_signature', key='F')
track.append(key_signature)

# Add notes to the track
time = 0
for note in notes:
    note_on = mido.Message('note_on', note=note, velocity=64, time=0)
    track.append(note_on)
    note_off = mido.Message('note_off', note=note, velocity=64, time=480)
    track.append(note_off)
    time += 480

# Save the MIDI file
mid.save('song.mid')
