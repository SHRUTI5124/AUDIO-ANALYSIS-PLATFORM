import speech_recognition as sr

def transcript():
# Initialize a recognizer instance
    r = sr.Recognizer()

    # Load the audio file
    audio_file = sr.AudioFile(r'static\audios\CantinaBand3.wav')

    # Use the recognizer to transcribe the audio file
    with audio_file as source:
        audio = r.record(source)

    text = r.recognize_google(audio)

    print(text)
