import speech_recognition as sr

# Initialize a recognizer instance
r = sr.Recognizer()

# Load the audio file
audio_file = sr.AudioFile('C:\Users\hp\OneDrive\Documents\web_app1\static\images\audios\02 Zaalima - Raees (Arijit Singh) 190kbps.wav')

# Use the recognizer to transcribe the audio file
with audio_file as source:
    audio = r.record(source)

text = r.recognize_google(audio)

print(text)
