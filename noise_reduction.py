import pvkoala
from file_conversion import convert_to_wav

def noise_reduction(audio):

    ACCESS_KEY='gkoTjQkgydcu+1wfNpjc9sCXijHkrUEqRsvkwwO8SOsiz7C8IJ7Log=='
    koala = pvkoala.create(access_key='${ACCESS_KEY}')


    def get_next_audio_frame():
        pass


    while True:
        enhanced_audio = koala.process(get_next_audio_frame())
    koala.reset()

if __name__ == '__main__':
    # mp3 to wav
    fp = r'static\audios\Recording.m4a'
    ep = convert_to_wav(fp, export_format='wav')
    print(ep)

    # call noise_reduction function
    noise_reduction(ep)

