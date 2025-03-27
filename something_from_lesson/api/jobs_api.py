import flask
import requests

from flask import Flask
from data import db_session
from data.jobs import Jobs


jobs_bp = flask.Blueprint("jobs_api", __name__, template_folder="templates")


@jobs_bp.route("/jobs")
def get_jobs():
    session = db_session.create_session()
    jobs = session.query(Jobs).all()
    return flask.jsonify({"jobs": ([item.to_dict(
        only=("id", "job", "team_leader", "work_size", "collaborators",
              "start_date", "end_date", "is_finished")
    ) for item in jobs])})


@jobs_bp.route("/jobs/<int:job_id>", methods=["GET"])
def get_jobs(job_id):
    session = db_session.create_session()
    jobs = session.query(Jobs).get(job_id)
    return flask.jsonify({"jobs": ([item.to_dict(
        only=("id", "job", "team_leader", "work_size", "collaborators",
              "start_date", "end_date", "is_finished")
    ) for item in jobs])})