import librosa
import numpy as np
import pandas as pd

# load the audio file
filename = 'horror-hit-logo-142395.mp3'
y, sr = librosa.load(filename)

# extract MFCCs
mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)
mfccs_mean = np.mean(mfccs, axis=1)
mfccs_std = np.std(mfccs, axis=1)

# extract spectral contrast
contrast = librosa.feature.spectral_contrast(y=y, sr=sr)
contrast_mean = np.mean(contrast, axis=1)
contrast_std = np.std(contrast, axis=1)

# extract chroma features
chroma = librosa.feature.chroma_stft(y=y, sr=sr)
chroma_mean = np.mean(chroma, axis=1)
chroma_std = np.std(chroma, axis=1)

# combine the features into a pandas DataFrame
df = pd.DataFrame({
    'mfccs_mean': mfccs_mean,
    'mfccs_std': mfccs_std,
    'contrast_mean': contrast_mean,
    'contrast_std': contrast_std,
    'chroma_mean': chroma_mean,
    'chroma_std': chroma_std,
})

# save the DataFrame to a CSV file
df.to_csv('features.csv', index=False)
