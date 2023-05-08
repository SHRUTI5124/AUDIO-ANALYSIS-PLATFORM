import pandas as pd
import librosa

# load the audio file and compute the tempo and beats
filename = r'static\audios\CantinaBand3.wav'
y, sr = librosa.load(filename)
tempo, beats = librosa.beat.beat_track(y=y, sr=sr)

# create a pandas DataFrame from the beats
df = pd.DataFrame({'beat_times': librosa.frames_to_time(beats, sr=sr)})

# export the DataFrame as a CSV file
df.to_csv('beats.csv', index=False)
