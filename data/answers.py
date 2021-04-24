import sqlalchemy
from .db_session import SqlAlchemyBase


class Answer(SqlAlchemyBase):
    __tablename__ = 'answers'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    post_id = sqlalchemy.Column(sqlalchemy.Integer)
    answering_to = sqlalchemy.Column(sqlalchemy.Integer)
    images = sqlalchemy.Column(sqlalchemy.PickleType)
    main_text = sqlalchemy.Column(sqlalchemy.String)
    date = sqlalchemy.Column(sqlalchemy.String)
    time = sqlalchemy.Column(sqlalchemy.String)
