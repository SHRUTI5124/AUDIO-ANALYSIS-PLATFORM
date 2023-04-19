from flask import Flask, render_template
import librosa

app = Flask(__name__)

@app.route('/')
def index():
    # load the audio file and compute the tempo
    filename = 'example.wav'
    y, sr = librosa.load(filename)
    tempo = librosa.beat.tempo(y=y, sr=sr)

    # render the template with the tempo
    return render_template('tempo.html', tempo=tempo)

if __name__ == '__main__':
    app.run()
