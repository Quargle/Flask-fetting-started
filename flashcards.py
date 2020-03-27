from flask import Flask
from datetime import datetime


app = Flask(__name__)   # in this case, passes "flashcards"


@app.route("/")
def welcome():
    return "Welcome to my Flash Cards application!"


counter = 0


@app.route("/views")
def count_views():
    global counter
    counter += 1    # This function is called every time the server attempts to call this page
    return f"This page has been viewed {counter} times."


@app.route("/date")
def date():
    return f"This page was served at {datetime.now()}"
