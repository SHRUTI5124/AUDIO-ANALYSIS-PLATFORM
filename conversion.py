from pydub import AudioSegment

def conversion():
    # Load the audio file
    audio_file = AudioSegment.from_file("input_file.mp3", format="mp3")

    # Export the audio file in WAV format
    audio_file.export("output_file.wav", format="wav")

if _main_ == '_main_':
    conversion()
