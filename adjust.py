import numpy as np
import librosa
from scipy.io import wavfile

# Load audio file
audio_file = f"instrumental/song/accompaniment.wav"
y, sr = librosa.load(audio_file, sr=None, mono=True)

y_mono = librosa.to_mono(y)


# Modify tempo and pitch
y_mod = librosa.effects.time_stretch(y_mono, rate=1.5) # Increase tempo by 20%
y_mod = librosa.effects.pitch_shift(y_mod, sr, n_steps=1) # Increase pitch by 1 semitone

# Convert waveform to spectrogram
n_fft = 2048
hop_length = 512
spec = librosa.stft(y_mod, n_fft=n_fft, hop_length=hop_length)

# Reconstruct audio with modified tempo and pitch
y_recon = librosa.griffinlim(spec, hop_length=hop_length)

# Save reconstructed audio as a WAV file
wavfile.write('modified_song.wav', sr, y_recon)