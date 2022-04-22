from flask import Flask
from flask import request
from flask import render_template
from turbo_flask import Turbo
import threading
import time
import random

app = Flask(__name__)

turbo = Turbo(app)

@app.route("/")
def main():
    return render_template("index.html")

translation = 0
@app.context_processor
def inject_load():
    translation = translation+1
    return {'translation': translation}

def update_load():
    with app.app_context():
        while True:
            time.sleep(5)
            turbo.push(turbo.replace(render_template('loadtranslation.html'), 'load'))

@app.before_first_request
def before_first_request():
    threading.Thread(target=update_load).start()