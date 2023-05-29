import wave
from textblob import TextBlob
from file_conversion import convert_to_wav
from transcript import transcript
import os


def analyse_sentiments(audio_file_path):

    # check file type and if not wav, convert to wav
    if audio_file_path.endswith('.wav'):
        wav_path = audio_file_path
    else:
        wav_path = audio_file_path[:-4] + '.wav'
        convert_to_wav(audio_file_path, wav_path)
    
    # get transcript
    transcript_text = transcript(wav_path)
    blob = TextBlob(transcript_text)

    # get sentiment
    sentiment = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    return sentiment , subjectivity


if __name__ == "__main__":
   analyse= analyse_sentiments(r'recording.wav')[0]
   print(analyse)

