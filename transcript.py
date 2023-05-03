import pvleopard

access_key = 'fHmV8BUYf1JCPxJ/W+JKDL+4KvlYafOtLTmRoQdP91Fb/dpEz4ZkPQ=='
def transcript(audio_path):
    handle = pvleopard.create(access_key)
    transcript, words = handle.process_file(audio_path)
    return transcript, words


if __name__=='__main__':
    text,words = transcript(r'static\audios\recording.m4a')
    print(text)