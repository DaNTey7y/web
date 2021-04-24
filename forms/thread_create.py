from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class ThreadCreateForm(FlaskForm):
    title = StringField('Название треда', validators=[DataRequired()])
    theme = StringField('Тема треда в двух словах', validators=[DataRequired()])
    text = TextAreaField('Ваш текст...', validators=[DataRequired()])
    image_1 = FileField('Можете добавить несколько фото',
                        validators=[FileAllowed(['png', 'jpg', 'jpeg'],
                                                'Только png, jpg и jpeg')],)
    image_2 = FileField(validators=[FileAllowed(['png', 'jpg', 'jpeg'], 'Только png, jpg и jpeg')])
    image_3 = FileField(validators=[FileAllowed(['png', 'jpg', 'jpeg'],
                                                'Только png, jpg и jpeg')])
    image_4 = FileField(validators=[FileAllowed(['png', 'jpg', 'jpeg'],
                                                'Только png, jpg и jpeg')])
    submit = SubmitField('Опубликовать')
