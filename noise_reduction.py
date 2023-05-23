
from file_conversion import convert_to_wav
import struct
import wave

from pvkoala import create, KoalaActivationLimitError

PROGRESS_BAR_LENGTH = 30


def noise_reduction(audio_input, audio_output):

    ACCESS_KEY='gkoTjQkgydcu+1wfNpjc9sCXijHkrUEqRsvkwwO8SOsiz7C8IJ7Log=='
    koala = create(access_key=ACCESS_KEY)
    length_sec = 0.0
    try:
        print('Koala version: %s' % koala.version)

        with wave.open(audio_input, 'rb') as input_file:
            if input_file.getframerate() != koala.sample_rate:
                raise ValueError('Invalid sample rate of `%d`. Koala only accepts `%d`' % (
                    input_file.getframerate(),
                    koala.sample_rate))
            if input_file.getnchannels() != 1:
                raise ValueError('This demo can only process single-channel WAV files')
            if input_file.getsampwidth() != 2:
                raise ValueError('This demo can only process WAV files with 16-bit PCM encoding')
            input_length = input_file.getnframes()

            with wave.open(audio_output, 'wb') as output_file:
                output_file.setnchannels(1)
                output_file.setsampwidth(2)
                output_file.setframerate(koala.sample_rate)

                start_sample = 0
                while start_sample < input_length + koala.delay_sample:
                    end_sample = start_sample + koala.frame_length

                    frame_buffer = input_file.readframes(koala.frame_length)
                    num_samples_read = len(frame_buffer) // struct.calcsize('h')
                    input_frame = struct.unpack('%dh' % num_samples_read, frame_buffer)
                    if num_samples_read < koala.frame_length:
                        input_frame = input_frame + (0,) * (koala.frame_length - num_samples_read)

                    output_frame = koala.process(input_frame)

                    if end_sample > koala.delay_sample:
                        if end_sample > input_length + koala.delay_sample:
                            output_frame = output_frame[:input_length + koala.delay_sample - start_sample]
                        if start_sample < koala.delay_sample:
                            output_frame = output_frame[koala.delay_sample - start_sample:]
                        output_file.writeframes(struct.pack('%dh' % len(output_frame), *output_frame))
                        length_sec += len(output_frame) / koala.sample_rate

                    start_sample = end_sample
                    progress = start_sample / (input_length + koala.delay_sample)
                    bar_length = int(progress * PROGRESS_BAR_LENGTH)
                    print(
                        '\r[%3d%%]|%s%s|' % (
                            progress * 100,
                            '#' * bar_length,
                            ' ' * (PROGRESS_BAR_LENGTH - bar_length)),
                        end='',
                        flush=True)

                print()

    except KeyboardInterrupt:
        print()
    except KoalaActivationLimitError:
        print('AccessKey has reached its processing limit')
    finally:
        if length_sec > 0:
            print('%.2f seconds of audio have been written to %s.' % (length_sec, audio_output))
        koala.delete()


if __name__ == '__main__':
    # mp3 to wav
    fp = r'static\audios\Recording.m4a'
    convert_to_wav(fp, 'static/generated/output_file.wav')
    # call noise_reduction function
    noise_reduction('static/generated/output_file.wav', 'static/generated/noiseless_file.wav')

