from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import plotly.express as px
from database import audio
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from werkzeug.utils import secure_filename
from mfccspectrogram import extract, spectrogram
from similarity_search import similar_search
from transcript import transcript as tscript
from file_conversion import convert_to_wav
from audio_enhancement import audio_enhancement
from analyse_sentiments import analyse_sentiments
from classification import query as query
from noise_reduction import noise_reduction
from wav_playback import playback

app = Flask(__name__)
app.secret_key = "Secret Key"

def getdb():
    engine = create_engine('sqlite:///project.sqlite')
    DBSession = sessionmaker(bind=engine)
    session = scoped_session(DBSession)
    return session

# home page
@app.route('/')
def home():
    name = "AUDIO ANALYSIS PLATFORM"
    return render_template('index.html', title=name)

# about page
@app.route('/about')
def about():
    return render_template('About1.html')

# registrartion 
@app.route('/registration', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        print(username, email, password)
        return redirect(url_for('home'))
    return render_template('registration.html')

# upload audio
@app.route('/audio/add', methods=['GET', 'POST'])
def add_audio():
    if request.method == 'POST':
        audio_file = request.files.get('file')
        # validate the data
        if audio_file is None:
            print('No file attached in request')
            return jsonify({'error': 'Missing file'})
        # save the file in a folder
        filename = secure_filename(audio_file.filename)
        filepath = 'static/uploads/'+filename
        wavname = filename.split('.')[0] + '.wav'
        outpath = 'static/uploads/'+wavname
        print(audio_file)
        print(filepath)
        convert_to_wav(filepath, outpath)
        audio_file.save(outpath)
        print('file saved')
        # save the data in the database
        db = getdb()
        db.add(audio(name=wavname, audio_file=outpath))
        db.commit()
        db.close()
        print('data saved')
        return jsonify({'msg': 'File saved successfully'}) 

    return render_template('fileupload.html')

# dashboard
@app.route('/dashboard')
def dashboard():
    db = getdb()
    audios = db.query(audio).all()
    db.close()
    return render_template('dashboard.html', audios=audios, title='Dashboard')

# operations into the applications
@app.route('/audio/operations/<int:id>', methods=['GET', 'POST'])
def operations(id):
    db = getdb()
    item = db.query(audio).filter_by(id=id).first()
    db.close()
    return render_template('operations.html', title='Operations', audio=item, id=id)

#transcript
@app.route('/action/transcript/<int:id>', methods=['GET', 'POST'])
def transcript(id):
    db = getdb()
    item = db.query(audio).filter_by(id=id).first()
    db.close()
    result = tscript(item.audio_file)
    return render_template('transcript.html', title='Transcript', audio=item, result=result)

#mfccspectrogram
@app.route('/action/visualize/<int:id>', methods=['GET', 'POST'])
def visualize(id):
    db = getdb()
    item = db.query(audio).filter_by(id=id).first()
    db.close()
    result = extract(item.audio_file)
    result['mfcc_graph'] = result['mfcc_graph'].to_html()
    result['contrast_graph'] = result['contrast_graph'].to_html()
    result['chroma_graph'] = result['chroma_graph'].to_html()
    return render_template('visualize.html', title='Visualize', audio=item, result=result)

# enhance
@app.route('/action/enhance/<int:id>', methods=['GET', 'POST'])
def enhance(id):
    db = getdb()
    item = db.query(audio).filter_by(id=id).first()
    db.close()
    enhanced_file = audio_enhancement(item.audio_file)
    return render_template('enhance.html', title='Enhance', audio=item, enhanced_file=enhanced_file)

# sentiment analysis
@app.route('/action/sentiment/<int:id>', methods=['GET', 'POST'])
def sentiment(id):
    db = getdb()
    item = db.query(audio).filter_by(id=id).first()
    db.close()
    result = analyse_sentiments(item.audio_file)
    if result == 0:
        result = 'Nuetral'
    elif result > 0:
        result = 'Positive'
    else:
        result = 'Negative'
    return render_template('sentiment.html', title='Sentiment', audio=item, result=result)

# classification
@app.route('/action/classify/<int:id>', methods=['GET', 'POST'])
def classify(id):
    db = getdb()
    item = db.query(audio).filter_by(id=id).first()
    db.close()
    result = query(item.audio_file)
    return render_template('classify.html', title='Classification', audio=item, result=result)

#similarity search
@app.route('/action/similarity/<int:id>', methods=['GET', 'POST'])
def similarity(id):
    db = getdb()
    item = db.query(audio).filter_by(id=id).first()
    db.close()
    result = similar_search(item.audio_file)
    return render_template('similarity.html', title='Similarity', audio=item, result=result)

#fileconversion
@app.route('/action/fileconversion/<int:id>', methods=['GET', 'POST'])
def fileconversion(id):
    db = getdb()
    item = db.query(audio).filter_by(id=id).first()
    db.close()
    return render_template('fileconversion.html', title='File Conversion', audio=item)

#noise reduction
@app.route('/action/noisereduction/<int:id>', methods=['GET', 'POST'])
def noisereduction(id):
    db = getdb()
    item = db.query(audio).filter_by(id=id).first()
    db.close()
    result = noise_reduction(item.audio_file)
    return render_template('noisereduction.html', title='Noise Reduction', audio=item, result=result)

#playback
@app.route('/action/playback/<int:id>', methods=['GET', 'POST'])
def playback(id):
    db = getdb()
    item = db.query(audio).filter_by(id=id).first()
    db.close()
    return render_template('playback.html', title='Playback', audio=item)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000, debug=True)