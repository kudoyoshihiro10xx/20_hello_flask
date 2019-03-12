import random
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", message="Hi")


@app.route("/dice", methods=["GET"])
def dice():
    result = random.randint(1, 6)

    return render_template("dice.html", result=result)


@app.route("/greet/<username>", methods=["POST"])
def greet(username):
    return render_template("greet.html", xxx=username)  # 左側のusernameは引数、右側のusernameは入力値



if __name__ == '__main__':
    app.run(debug=True)
