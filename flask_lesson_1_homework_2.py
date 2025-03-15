from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    return "There are results of selecting"


@app.route("/results/<nickname>/<int:level>/<float:rating>")
def result(nickname, level, rating):
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
        crossorigin="anonymous">
    <title>Selecting_results</title>
    </head>
    <body>
        <h1>Результаты отбора</h1>
        <h2>Претендента на участие в мисси {}:</h2>
        <div class="alert alert-success" role="alert">
            <h3>Поздравляем! Ваш рейтинг полсе {} этапа отбора составляет:</h3>
        </div>
        <h3>{}!</h3>
        <div class="alert alert-warning" role="alert">
            <h3>Желаем Удачи!</h3>
        </div>
    </body>
    </html>
    """.format(nickname, level, rating)


if __name__ == "__main__":
    app.run("127.0.0.1", port=8080)