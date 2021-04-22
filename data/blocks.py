import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase


class Block(SqlAlchemyBase):
    __tablename__ = 'posts'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    type = sqlalchemy.Column(sqlalchemy.String)
