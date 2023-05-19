import librosa
import librosa.filters
import numpy as np
import scipy.signal
import soundfile as sf

# Load the audio file


def audio_enhancement(audio_file = r'static\audios\Recording.m4a'):         #to enhance the audio quality
    y, sr = librosa.load(audio_file)
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
    y = librosa.effects.core.mu_compress(y, mu=0.8, quantize=True)

    # Apply noise reduction
    # y = librosa.effects.reduce_noise(y)

    # Write the enhanced audio to file
    enhanced_file = 'enhanced_audio.wav'
    sf.write(enhanced_file, y, sr, subtype='PCM_24')
if __name__=='__main__':
    audio_enhancement()