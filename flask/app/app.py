from flask import Flask,render_template,request
from . import english,kanji

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
        result_en = english.main_en(user_input)  # 結果を取得
        return render_template("english.html", result=result_en)  # 結果を表示
    return render_template("english.html")

@app.route("/kanji/knpy", methods=["GET", "POST"])
def knpy():
    if request.method == "POST":
        user_input = request.form["user_input"]  # フォームからの入力を取得
        result_kn = kanji.main_kn(user_input)  # 結果を取得
        return render_template("kanji.html", result=result_kn)  # 結果を表示
    return render_template("kanji.html")