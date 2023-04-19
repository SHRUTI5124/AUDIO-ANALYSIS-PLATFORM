import pyaudio
import wave

# set up the audio file
filename = 'horror-hit-logo-142395.mp3.wav'
chunk = 1024

# open the file and create a PyAudio instance
wf = wave.open(filename, 'rb')
p = pyaudio.PyAudio()

# define the callback function for playing the audio
def callback(in_data, frame_count, time_info, status):
    data = wf.readframes(frame_count)
    return (data, pyaudio.paContinue)

# open the audio stream and start playing
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True,
                stream_callback=callback)

stream.start_stream()

# wait until the stream is finished
while stream.is_active():
    time.sleep(0.1)

# stop and close the stream and PyAudio instance
stream.stop_stream()
stream.close()
wf.close()
p.terminate()
