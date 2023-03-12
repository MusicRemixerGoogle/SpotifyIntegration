import mido

# Set the tempo (in BPM) and the time signature
tempo = 98
time_signature = (3, 4)

# Create a new MIDI file with one track
mid = mido.MidiFile()
track = mido.MidiTrack()
mid.tracks.append(track)

# Add the time signature and set the tempo
time_signature_msg = mido.MetaMessage('time_signature', numerator=time_signature[0], denominator=time_signature[1])
set_tempo_msg = mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(tempo))
track.append(time_signature_msg)
track.append(set_tempo_msg)

# Calculate the duration of one beat in ticks
ticks_per_beat = mid.ticks_per_beat
ticks_per_bar = ticks_per_beat * time_signature[0]
ticks_per_sixteenth = ticks_per_beat // 4

# Add a note-on and note-off message for each frequency
for freq in frequencies:
    # Calculate the duration of the note in ticks (e.g. a quarter note has a duration of ticks_per_beat)
    duration_in_beats = 0.25
    duration_in_ticks = int(duration_in_beats * ticks_per_beat)

    # Calculate the MIDI note number for the frequency (rounded to the nearest integer)
    note_number = int(round(12 * (math.log(freq / 440.0) / math.log(2)) + 69))

    # Create note-on and note-off messages with the calculated values
    note_on = mido.Message('note_on', note=note_number, velocity=64, time=0)
    note_off = mido.Message('note_off', note=note_number, velocity=0, time=duration_in_ticks)

    # Append the note-on and note-off messages to the track
    track.append(note_on)
    track.append(note_off)

# Save the MIDI file
mid.save('my_song.mid')