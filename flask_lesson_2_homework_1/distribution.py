from flask import Flask, render_template

app = Flask(__name__)


@app.route("/distribution")
def main():
    members = ["Владимир Примаков",
               "Цинь Шихуанди",
               "Илон Маск",
               "Марк Уотни",
               "Гарри Селдон",
               "Шон Бин",
               "Иванов Иван"]
    return render_template("distribution.html", members=members)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)