from leopard import Leopard 
from pvcheetah import Transcriber

def transcribe_audio(file_path):
    # Create a new Leopard or Cheetah instance
    # leopard = Leopard()
    # cheetah = Transcriber()
    
    # Load the audio file
    with open(file_path, "rb") as audio_file:
        audio_data = audio_file.read()
        
    # Transcribe the audio
    transcription = Leopard.transcribe(audio_data)
    transcription = pvcheetah.transcribe(audio_data) 
    
    # Return the transcription
    return transcription

transcription = transcribe_audio(r"static\audios\Recording.m4a")
print(transcription)
