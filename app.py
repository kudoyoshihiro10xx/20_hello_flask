import random
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", message="Hi")


@app.route("/dice", methods=["GET"])
def dice():
    result = random.randint(1, 6)

    return render_template("dice.html", yyy=result)


@app.route("/greet/<username>", methods=["POST"])
def greet(username):
    return render_template("greet.html", xxx=username)  # 左側のusernameは引数、右側のusernameは入力値


@app.route("/form", methods=["GET"])
def show_form():
    return render_template("form.html")


@app.route("/post_name", methods=["POST"])
def request_post():
    username = request.form["username"]
    return f"こんにちは {username}さん"


if __name__ == '__main__':
    app.run(debug=True)
