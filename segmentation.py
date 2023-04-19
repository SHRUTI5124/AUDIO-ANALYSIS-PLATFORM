import librosa
import numpy as np

# load the audio file
filename = 'example.wav'
y, sr = librosa.load(filename)

# calculate the energy envelope of the audio waveform
energy = np.abs(librosa.stft(y))**2
energies = librosa.feature.sync(energy, librosa.frames_to_samples(np.ones(len(energy))), aggregate=np.median)
env = np.mean(energies, axis=0)

# set the threshold for detecting changes in energy level
threshold = np.median(env) * 1.5

# initialize the segment boundaries
segments = []
start = 0

# iterate over the energy envelope and detect segment boundaries
for i in range(len(env)):
    if env[i] > threshold and i - start >= sr * 5: # minimum segment length of 5 seconds
        segments.append((start, i))
        start = i

# add the last segment
if start < len(env):
    segments.append((start, len(env)))

# iterate over the segments and classify them as verses or choruses
sections = []
for i in range(len(segments)):
    section = y[segments[i][0]:segments[i][1]]
    section_energy = np.abs(librosa.stft(section))**2
    section_energies = librosa.feature.sync(section_energy, librosa.frames_to_samples(np.ones(len(section_energy))), aggregate=np.median)
    section_env = np.mean(section_energies, axis=0)
    section_max = np.max(section_env)
    if section_max > np.median(env) * 2: # chorus threshold
        sections.append(('chorus', segments[i]))
    else:
        sections.append(('verse', segments[i]))

# print the results
for section in sections:
    print(section[0], section[1])
