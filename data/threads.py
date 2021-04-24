import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Thread(SqlAlchemyBase):
    __tablename__ = 'threads'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    post_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("posts.id"))
    images = sqlalchemy.Column(sqlalchemy.PickleType)
    title = sqlalchemy.Column(sqlalchemy.String, index=True)
    theme = sqlalchemy.Column(sqlalchemy.String)
    main_text = sqlalchemy.Column(sqlalchemy.String)
    answers_amount = sqlalchemy.Column(sqlalchemy.Integer)
    date = sqlalchemy.Column(sqlalchemy.String)
    time = sqlalchemy.Column(sqlalchemy.String)
    post = orm.relation('Post')
