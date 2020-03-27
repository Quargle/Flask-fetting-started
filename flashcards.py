from flask import Flask, render_template


app = Flask(__name__)   # in this case, passes "flashcards"


@app.route("/")
def welcome():
    return render_template("welcome.html")



