import datetime
import sqlalchemy
from sqlalchemy import orm


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    team_leader = sqlalchemy.Column(sqlalchemy.Integer)
    job = sqlalchemy.Column(sqlalchemy.String)
    work_size = sqlalchemy.Column(sqlalchemy.Integer)
    collaborators = sqlalchemy.Column(sqlalchemy.String)
    start_date = sqlalchemy.Column(sqlalchemy.DATE,
                                   default=datetime.date.today())
    end_date = sqlalchemy.Column(sqlalchemy.DATE,
                                 default=datetime.date.today())
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean)