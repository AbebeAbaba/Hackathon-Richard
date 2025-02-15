from flask import Flask,render_template
from . import english

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/english")
def en():
    return render_template("english.html")

@app.route("/kanji")
def kanji():
    return render_template("kanji.html")

@app.route("/english/enpy")
def enpy():
    return english.main()