import matplotlib.pyplot as plt
import librosa
import numpy as np

# load the audio file and compute the spectrogram
filename = r'static\audios\CantinaBand3.wav'
y, sr = librosa.load(filename)
spec = librosa.feature.melspectrogram(y=y, sr=sr)

# plot the spectrogram
plt.figure(figsize=(10, 4))
librosa.display.specshow(librosa.power_to_db(spec, ref=np.max),
                         y_axis='mel', fmax=8000,
                         x_axis='time')
plt.colorbar(format='%+2.0f dB')
plt.title('Mel spectrogram')
plt.tight_layout()

# save the plot as a PNG image
plt.savefig('mel_spec.png')
