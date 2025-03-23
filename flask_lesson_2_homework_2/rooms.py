from flask import Flask, render_template

app = Flask(__name__)


@app.route("/table/<gender>/<int:age>")
def main(gender, age):
    return render_template("rooms.html", gender=gender, age=age)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)