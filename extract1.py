import librosa
import numpy as np
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt


def extract():
    # load the audio file
    filename = r'static\audios\CantinaBand3.wav'
    y, sr = librosa.load(filename)

    # extract MFCCs
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=100)
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

    # plot the features
    fig, axs = plt.subplots(3, 1, figsize=(15, 10))
    sns.barplot(x=np.arange(1, 21), y=mfccs_mean, ax=axs[0],)
    sns.barplot(x=np.arange(1, 21), y=mfccs_std, ax=axs[1]) 
    sns.barplot(x=np.arange(1, 21), y=mfccs_mean, ax=axs[2])
    plt.savefig('static\images\mfccs.png', bbox_inches='tight')

    # plot line graph
    fig, axs = plt.subplots(3, 1, figsize=(15, 10))
    sns.lineplot(x=np.arange(1, 21), y=mfccs_mean, ax=axs[0],)
    sns.lineplot(x=np.arange(1, 21), y=mfccs_std, ax=axs[1])
    sns.lineplot(x=np.arange(1, 21), y=mfccs_mean, ax=axs[2])
    plt.savefig('static\images\mfccs_line.png', bbox_inches='tight')
    return mfccs , contrast, chroma

def spectrogram(mfccs , contrast , chroma):                          #plot spectrogram
    fig, axs = plt.subplots(3, 1, figsize=(15, 10))
    sns.heatmap(mfccs, ax=axs[0])
    sns.heatmap(contrast, ax=axs[1])
    sns.heatmap(chroma, ax=axs[2])
    plt.savefig('static\images\mfccs_heatmap.png', bbox_inches='tight')

def plotly_spectrogram(mfccs , contrast , chroma):                   #plot spectrogram using plotly
    fig = px.imshow(mfccs)
    fig.show()

extract()
mfccs , contrast, chroma = extract()
spectrogram(mfccs , contrast, chroma)
plotly_spectrogram(mfccs , contrast,chroma)