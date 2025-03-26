from flask import Flask, render_template
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


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


def main():
    db_session.global_init("db/mars.db")

    app.run(host="127.0.0.1", port=8080)


if __name__ == '__main__':
    main()