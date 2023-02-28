from twisty import app
from flask import Response

@app.route("/")
def index():
    return Response("Index page.")
