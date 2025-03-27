from flask import Flask, render_template, redirect
from flask_login import login_user, LoginManager, login_required, logout_user

from data import db_session
from data.users import User
from data.jobs import Jobs
from data.departments import Department
from data.login_form import LoginForm
from data.register_form import RegisterForm

from sqlalchemy import select, func

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    session = db_session.create_session()
    return session.query(User).get(user_id)


@app.route("/")
def index():
    session = db_session.create_session()
    query = session.query(Jobs)
    jobs = []

    for job in query:
        team_leader_id = job.team_leader
        team_leader = session.query(User.name).filter(User.id == team_leader_id).first()[0]
        some_job = [job.job, team_leader, job.work_size, job.collaborators, job.is_finished]
        jobs.append(some_job)

    return render_template("actions.html", jobs=jobs)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        user = session.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
        return redirect("/")
    return render_template("login.html", title="Authorisation", form=form)


@app.route("/logout")
@login_required
def logout():
    logaut_user()
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.password.data != form.repeat_password.data:
        return render_template("register.html", title="Регистрация",
                               message="Пароли не совпадают", form=form)

    session = db_session.create_session()
    if form.validate_on_submit():
        if session.query(User).filter(User.email == form.email.data).first():
            return render_template("register.html", title="Регистрация",
                               message="Такой пользователь уже существует", form=form)

        user = User(
            name=form.name.data,
            surname=form.surname.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data,
            email=form.email.data
        )
        user.set_password(form.password.data)
        session.add(user)
        session.commit()
        return redirect("/")
    return render_template("register.html", title="Registration", form=form)


def main():
    db_session.global_init("db/mars.db")
    app.run(host="127.0.0.1", port=8080)


if __name__ == '__main__':
    main()