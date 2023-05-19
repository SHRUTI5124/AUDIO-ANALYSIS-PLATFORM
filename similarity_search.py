import librosa
import numpy as np
import plotly.express as px
# Load the audio files


def similar_search(audio_file1, audio_file2):         # Extract features from the audio files
    features1 = librosa.feature.mfcc(y=audio_file1, sr=22050)
    features2 = librosa.feature.mfcc(y=audio_file2, sr=22050)

    # Calculate the similarity between the features using cosine similarity
    similarity = np.dot(features1.T, features2) / np.linalg.norm(features1) / np.linalg.norm(features2)

    print('Similarity between the two audio files: ', similarity)
    # plot
    mean = np.mean(similarity)
    std = np.std(similarity)

    fig = px.imshow(similarity, color_continuous_scale='gray')
    fig.update_layout(title=f'Similarity between the two audio files mean={mean:.2f}, std={std:.2f}')
    return fig


if __name__=='__main__':
    audio_file1 = librosa.load(r'static\audios\CantinaBand3.wav')[0]
    audio_file2 = librosa.load(r'static\audios\CantinaBand3.wav')[0]
    fig = similar_search(audio_file1, audio_file2)
    fig.show()