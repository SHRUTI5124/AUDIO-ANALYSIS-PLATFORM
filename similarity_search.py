import librosa
import numpy as np

# Load the audio files
audio_file1 = librosa.load(r'static\audios\CantinaBand3.wav')[0]
audio_file2 = librosa.load(r'static\audios\CantinaBand3.wav')[0]


def similar_search():         # Extract features from the audio files
    features1 = librosa.feature.mfcc(y=audio_file1, sr=22050)
    features2 = librosa.feature.mfcc(y=audio_file2, sr=22050)

    # Calculate the similarity between the features using cosine similarity
    similarity = np.dot(features1.T, features2) / np.linalg.norm(features1) / np.linalg.norm(features2)

    print('Similarity between the two audio files: ', similarity)
