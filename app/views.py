from flask import render_template
from app import app


@app.route('/')
def index():
    message = 'hello flask'
    return render_template('index.html', message=message)


@app.route('pitches.html')
def pitches():
    '''
    will return pitches page and its details
    '''
    return render_template('pitches.html')
