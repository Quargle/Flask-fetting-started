from flask import Flask, render_template
from model import db

app = Flask(__name__)   # in this case, passes "flashcards"


@app.route("/")
def welcome():
    return render_template(
        "welcome.html",
        message="Here's a message from the view function."
    )


@app.route("/card")
def card_view():
    card = db[0]
    return render_template("card.html", card=card)
