from flask import Flask, render_template

app = Flask(__name__)


@app.route("/answer")
@app.route("/auto_answer")
def answer():
    dictionary = {
        "title": "answer",
        "surname": "Иванов",
        "name": "Иван",
        "education": "высшее",
        "profession": "Гастроэнтеролог",
        "sex": "Мужской",
        "motivation": "С таким-то именем, зачем на земле оставаться",
        "ready": "Да!"
    }

    return render_template("auto_answer.html", **dictionary)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)