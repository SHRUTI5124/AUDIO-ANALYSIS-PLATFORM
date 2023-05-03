import librosa
import librosa.filters
import numpy as np
import scipy.signal

# Load the audio file
audio_file = r'static\audios\CantinaBand3.wav'
y, sr = librosa.load(audio_file)

def audio_enhancement():         #to enhance the audio quality
    y, sr = librosa.load(audio_file)

    # Apply pre-emphasis filter
    pre_emphasis = 0.97
    y = np.append(y[0], y[1:] - pre_emphasis * y[:-1])

    # Apply a high-pass filter
    cutoff_hz = 100
    b, a = scipy.signal.butter(4, cutoff_hz / (sr / 2), 'highpass')
    y = scipy.signal.filtfilt(b, a, y)

    # Apply a low-pass filter
    cutoff_hz = 4000
    b, a = scipy.signal.butter(4, cutoff_hz / (sr / 2), 'lowpass')
    y = scipy.signal.filtfilt(b, a, y)

    # Remove silence
    y, _ = librosa.effects.trim(y)

    # Apply dynamic range compression
    y = librosa.effects.compress_dynamic_range(y)

    # Apply noise reduction
    y = librosa.effects.reduce_noise(y)
    # Write the enhanced audio to file
    enhanced_file = 'path/to/enhanced_audio.wav'
    librosa.output.write_wav(enhanced_file,y,sr)