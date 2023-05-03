from pydub import AudioSegment
import os
def conversion(file_path,export_path="output_file.wav", export_format='wav'):
    format=os.path.splitext(file_path)[-1].replace('.','')
    audio_file = AudioSegment.from_file(file_path, format=format)
    save_folder = 'static/generated'
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
    export_path = os.path.join(save_folder, export_path)
    audio_file.export(export_path, format=export_format)
    return export_path

if __name__ == '__main__':
    # mp3 to wav
    fp = r'static\audios\relaxing-145038.mp3'
    ep = conversion(fp, export_path='output_file.wav', export_format='wav')
    print(ep)

    # wav to mp3
    fp = r'static\audios\CantinaBand3.wav'
    ep = conversion(fp, export_path='output_file.mp3', export_format='mp3')