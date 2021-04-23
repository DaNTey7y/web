import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Thread(SqlAlchemyBase):
    __tablename__ = 'threads'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    post_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("posts.id"))
    title = sqlalchemy.Column(sqlalchemy.String, index=True)
    # themes = sqlalchemy
    # images = sqlalchemy.Column()
    main_text = sqlalchemy.Column(sqlalchemy.String)
    answers_amount = sqlalchemy.Column(sqlalchemy.Integer)
    post = orm.relation('Post')
