import struct
import wave

from pvcheetah import CheetahActivationLimitError, create

audio_file = r"static\audios\sunrise-anna-li-sky-wav-8476.mp3"
access_key='gkoTjQkgydcu+1wfNpjc9sCXijHkrUEqRsvkwwO8SOsiz7C8IJ7Log=='
#to transcript the audio file
def transcript(wav_path):
    try:
        o = create(
        access_key=access_key,
        enable_automatic_punctuation=True)
        with wave.open(wav_path, 'rb') as f:
            if f.getframerate() != o.sample_rate:
                raise ValueError(
                    "invalid sample rate of `%d`. cheetah only accepts `%d`" % (f.getframerate(), o.sample_rate))
            if f.getnchannels() != 1:
                raise ValueError("Can only process single-channel WAV files")
            if f.getsampwidth() != 2:
                raise ValueError("Can only process 16-bit WAV files")

            buffer = f.readframes(f.getnframes())
            audio = struct.unpack('%dh' % (len(buffer) / struct.calcsize('h')), buffer)

        num_frames = len(audio) // o.frame_length
        transcript = ''
        for i in range(num_frames):
            frame = audio[i * o.frame_length:(i + 1) * o.frame_length]
            partial_transcript, _ = o.process(frame)
            print(partial_transcript, end='', flush=True)
            transcript += partial_transcript
        final_transcript = o.flush()
        return transcript
    except CheetahActivationLimitError:
        print("Activation limit reached")
    except Exception as e:
        print("Error: %s" % e)
        

if __name__ == "__main__":
    result = transcript(r'recording.wav')
    print(result)