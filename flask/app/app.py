from flask import Flask,render_template,request
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

@app.route("/english/enpy", methods=["GET", "POST"])
def enpy():
    if request.method == "POST":
        user_input = request.form["user_input"]  # フォームからの入力を取得
        result = english.main(user_input)  # 結果を取得
        return render_template("english.html", result=result)  # 結果を表示
    return render_template("english.html")