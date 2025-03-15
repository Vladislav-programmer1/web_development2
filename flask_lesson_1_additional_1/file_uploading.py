from flask import Flask, request, url_for
from PIL import Image
from io import BytesIO

app = Flask(__name__)


@app.route("/load_photo", methods=["POST", "GET"])
def load_photo():
    if request.method == "POST":
        try:
            f = request.files["file"]
            image = Image.open(BytesIO(f.read()))
            image = image.resize((200, 200))
            image.save("static/img/current.png")
        except Exception:
            pass
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
        crossorigin="anonymous">
        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
        <title>Title</title>
    </head>
    <body>
        <h1>Загрузка фотографии</h1>
        <h3>для участия в миссии</h3>
        <div>
            <form class="login_form" method="post" enctype="multipart/form-data">
                <div class="form-group">
                    <label for="photo">Приложите фотографию</label>
                    <input type="file" class="form-control-file" id="photo" name="file">
                </div>
                <div>
                    <img src="static/img/current.png">
                </div>
                <button type="submit" class="btn btn-primary">Отправить</button>
            </form>
        </div>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)