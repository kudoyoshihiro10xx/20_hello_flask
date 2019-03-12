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


if __name__ == '__main__':
    app.run(debug=True)
