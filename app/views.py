from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    options = {
        1 : "Water",
        2 : "Fire",
        3 : "Grass",
        4 : "Fairy"
    }
    return render_template('index.html', options=options)
