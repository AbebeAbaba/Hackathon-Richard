from flask import Flask,render_template,request
from . import english,kanji
import json

app = Flask(__name__)

#ホーム
@app.route("/")
def index():
    return render_template("index.html")

#英語
@app.route("/english")
def en():
    return render_template("english.html")

#漢字
@app.route("/kanji")
def kn():
    return render_template("kanji.html")

#英語入出力
@app.route("/english/enpy", methods=["GET", "POST"])
def enpy():
    if request.method == "POST":
        user_input_en = request.form["user_input"]  #フォームからの入力を取得
        result_en = english.main_en(user_input_en)  #結果を取得
        return render_template("english.html", result=result_en)  #結果を表示

#漢字入出力
@app.route("/kanji/knpy", methods=["GET", "POST"])
def knpy():
    if request.method == "POST":
        user_input_kn = request.form["user_input"]  #フォームからの入力を取得
        result_kn = kanji.main_kn(user_input_kn)  #結果を取得
        return render_template("kanji.html", result=result_kn)  #結果を表示
    return render_template("kanji.html")

#ヘルプ画面
@app.route("/help")
def help():
    with open('list.json', 'r', encoding='utf-8') as words:
        data = json.load(words)
    return render_template("help.html", list_data=data)