from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FileField
from wtforms.validators import DataRequired


class ThreadCreateForm(FlaskForm):
    title = StringField('Название треда', validators=[DataRequired()])
    theme = StringField('Тема треда в двух словах', validators=[DataRequired()])
    text = TextAreaField('Ваш текст...', validators=[DataRequired()])
    image_1 = FileField('Можете добавить несколько фото')
    image_2 = FileField()
    image_3 = FileField()
    image_4 = FileField()
    submit = SubmitField('Опубликовать')
