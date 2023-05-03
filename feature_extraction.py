import librosa

# Load the audio file
audio_file = r'static\audios\CantinaBand3.wav'
y, sr = librosa.load(audio_file)

def feature_extraction():                    # Estimate the pitch
    pitch, _ = librosa.core.pitch.piptrack(y=y, sr=sr)
    estimated_pitch = librosa.core.pitch.pitch_frequencies(pitch, sr=sr)[0]

    print('Estimated pitch:', estimated_pitch)

    # Estimate the tempo
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    print('Estimated tempo:', tempo)

    # Extract the melody
    melody = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=12)
<<<<<<< HEAD
    print('Melody:', melody)

    
if __name__=='__main__':
    feature_extraction()
=======
    print('Melody:',melody)
>>>>>>> f0fc8b471be77c76969d6121908ec975e8fdc59a
