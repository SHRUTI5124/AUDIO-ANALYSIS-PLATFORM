from flask import Flask, render_template, request, redirect
import plotly.express as px
from database import audio
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from werkzeug.utils import secure_filename

app = Flask(__name__)

def getdb():
    engine = create_engine('sqlite:///project.sqlite')
    DBSession = sessionmaker(bind=engine)
    session = scoped_session(DBSession)
    return session

def load_gapminder():
    df = px.data.gapminder()
    return df

@app.route('/')
def home():
    name = "AUDIO ANALYSIS PLATFORM"
    return render_template('main.html', title=name)

@app.route('/about')
def about():
    return render_template('About1.html')

@app.route('/audio/add', methods=['GET', 'POST'])
def add_audio():
    if request.method == 'POST':
        name = request.form.get('name')
        audio_file = request.files.get('audio_file')
        # validate the data
        if len(name) == 0 or audio_file is None:
            print("Please fill all the fields")
            return redirect('/audio/add')
        # save the file in a folder
        filename = secure_filename(audio_file.filename)
        filepath = 'static/uploads/'+filename
        audio_file.save(filepath)
        print('file saved')
        # save the data in the database
        db = getdb()
        db.add(audio(name=name, audio_file=filepath))
        db.commit()
        db.close()
        print('data saved')
        return redirect('/audio/add') 

    return render_template('audio.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000, debug=True)
 