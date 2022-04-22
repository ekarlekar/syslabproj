from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def main():
    return "<p>Esha did not do anything</p>"

translation = 0
@app.context_processor
def inject_load():
    translation +=1
    return {'translation': translation}