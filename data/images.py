import sqlalchemy
from .db_session import SqlAlchemyBase


class Image(SqlAlchemyBase):
    __tablename__ = 'images'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    post_id = sqlalchemy.Column(sqlalchemy.Integer)
    title = sqlalchemy.Column(sqlalchemy.String)
    file_path = sqlalchemy.Column(sqlalchemy.String)
