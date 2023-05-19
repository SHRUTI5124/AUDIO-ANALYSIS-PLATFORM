from os import path
from pydub import AudioSegment

def convert_to_wav(input_file, output_file, fr=16000, ch=1):
    """
    Converts an audio file to WAV format using pydub library.
    :param input_file: Path to the input audio file.
    :param output_file: Path to save the output WAV file.
    :return: True if the conversion was successful, False otherwise.
    """
    # Check if the input file exists
    if not path.isfile(input_file):
        print(f"Error: File '{input_file}' does not exist.")
        return False
    
    # Check if the output file already exists
    if path.isfile(output_file):
        print(f"Warning: File '{output_file}' already exists and will be overwritten.")
    
    try:
        # Convert the file to WAV format of 16000
        sound = AudioSegment.from_file(input_file)
        sound = sound.set_frame_rate(fr)
        sound = sound.set_channels(ch)
        sound.export(output_file, format="wav")
    except Exception as e:
        print(f"Error: {e}")
        return False
    
    print(f"Successfully converted '{input_file}' to '{output_file}'.")
    return True

# input_file = r"C:\Users\hp\OneDrive\Documents\web_app1\static\audios\Recording.m4a"
# output_file = "recording.wav"

# result = convert_to_wav(input_file, output_file)

# if result:
#     print("Conversion was successful!")
# else:
#     print("Conversion failed.")

if __name__=='__main__':
    convert_to_wav(input_file, output_file)