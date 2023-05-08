from leopard import Leopard 
from pvcheetah import Transcriber

audio_file = r"static\audios\sunrise-anna-li-sky-wav-8476.mp3"

#to transcript the audio file
def transcript(audio_file):
    #transcript audio file
    transcript = Transcriber(audio_file)
    transcript.transcript()
    #load the transcript file
    leopard = Leopard('transcript.txt')
    #return the transcript
    return leopard.get_transcript()

if __name__ == "__main__":
    transcript(audio_file)