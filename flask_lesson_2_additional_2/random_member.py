from flask import Flask, render_template
from json import load

app = Flask(__name__)


@app.route("/member")
def main():
    with open("templates/members.json", "r", encoding="UTF-8") as members_file:
        members = load(members_file)
    return render_template("members.html", members=members["members"])


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)