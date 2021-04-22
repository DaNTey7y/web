import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase


class Thread(SqlAlchemyBase):
    __tablename__ = 'threads'

    # id = sqlalchemy.Column(sqlalchemy.Integer,
    #                        primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, index=True)
    # author
    # themes = sqlalchemy
    description = sqlalchemy.Column(sqlalchemy.String)
    # images = sqlalchemy.Column()
    main_text = sqlalchemy.Column(sqlalchemy.String)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now)
    answers_amount = sqlalchemy.Column(sqlalchemy.Integer)
