from flask import Flask

app = Flask(__name__)

@app.route("/")
def root():
    return "<a href='https://github.com/justTrueCodeWriter/twisty'>Twisty</a>"
