from flask import Flask, render_template

app = Flask(__name__)


@app.route("/<list_>")
@app.route("/index/<list_>")
def main(list_):
    return render_template("task3.html", list=list_)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)