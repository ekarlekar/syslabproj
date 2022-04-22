from flask import Flask
from flask import request
from flask import render_template
from turbo_flask import Turbo
import threading
import time
import random
import os

app = Flask(__name__)

turbo = Turbo(app)

@app.route("/")
def main():
    return render_template("index.html")

@app.context_processor
def inject_load():
    with open('translated_output.txt', 'r') as f:
        translation = f.readlines()[-1]
    return {'translation': translation}

def update_load():
    filename = "translated_output.txt"
    with app.app_context():
        stamp = os.stat(filename).st_mtime
        while True:
            if os.stat(filename).st_mtime != stamp:
                turbo.push(turbo.replace(render_template('loadtranslation.html'), 'load'))
                stamp = os.stat(filename).st_mtime

@app.before_first_request
def before_first_request():
    threading.Thread(target=update_load).start()