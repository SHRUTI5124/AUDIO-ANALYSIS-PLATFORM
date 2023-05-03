import pvkoala

def noise_reduction(audio):

    ACCESS_KEY='fHmV8BUYf1JCPxJ/W+JKDL+4KvlYafOtLTmRoQdP91Fb/dpEz4ZkPQ=='
    koala = pvkoala.create(access_key='${ACCESS_KEY}')


    def get_next_audio_frame():
        pass


    while True:
        enhanced_audio = koala.process(get_next_audio_frame())
    koala.reset()

if __name__ == '__main__':
    # mp3 to wav
    fp = r'static\audios\relaxing-145038.mp3'
    ep = conversion(fp, export_path='output_file.wav', export_format='wav')
    print(ep)

    # wav to mp3
    fp = r'static\audios\CantinaBand3.wav'
    ep = conversion(fp, export_path='output_file.mp3', export_format='mp3')