from flask import Flask, render_template
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
def index():
    return render_template("index.html")


def main():
    db_session.global_init("db/mars.db")
    session = db_session.create_session()

    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    session.add(user)

    user = User()
    user.surname = "Smith"
    user.name = "Alex"
    user.age = 41
    user.position = "not captain"
    user.speciality = "builder"
    user.address = "module_2"
    user.email = "smith@mars.org"
    session.add(user)

    user = User()
    user.surname = "Uorhol"
    user.name = "Ende"
    user.age = 35
    user.position = "not captain"
    user.speciality = "drawer"
    user.address = "module_3"
    user.email = "uorhol@mars.org"
    session.add(user)

    user = User()
    user.surname = "Boucher"
    user.name = "Rid"
    user.age = 29
    user.position = "not captain"
    user.speciality = "doctor"
    user.address = "module_4"
    user.email = "boucher@mars.org"
    session.add(user)

    user = User()
    user.surname = "Komtua"
    user.name = "Jhon"
    user.age = 36
    user.position = "not captain"
    user.speciality = "biologist"
    user.address = "module_5"
    user.email = "komtua@mars.org"
    session.add(user)
    session.commit()

    # app.run(host="127.0.0.1", port=8080)


if __name__ == '__main__':
    main()