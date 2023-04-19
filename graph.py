import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt

# Generate a sine wave with a frequency of 440 Hz and a duration of 1 second
sampling_rate = 22050
duration = 1
frequency = 440
samples = np.arange(sampling_rate * duration)
audio = np.sin(2 * np.pi * frequency * samples / sampling_rate)

# Compute the spectrogram using a short-time Fourier transform (STFT)
stft = librosa.stft(audio)

# Convert the STFT to a power spectrogram
spec = librosa.power_to_db(np.abs(stft)**2)

# Display the spectrogram
plt.figure(figsize=(10, 4))
librosa.display.specshow(spec, sr=sampling_rate, x_axis='time', y_axis='hz')
plt.colorbar()
plt.title('Spectrogram of Audio Signal')
plt.tight_layout()
plt.show()
