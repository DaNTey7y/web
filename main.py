import os
from flask import Flask, render_template, redirect
from datetime import datetime
from data import db_session
from data.posts import Post
from data.threads import Thread
from data.functions import generate_s, form_text
from data.images import Image
from data.answers import Answer
from forms.thread_create import ThreadCreateForm
from forms.answer import AnswerForm
from sqlalchemy import desc
from werkzeug.utils import secure_filename


app = Flask(__name__)


# Главная страница, где выводятся все треды

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home_page():
    db_sess = db_session.create_session()
    params = dict()
    params['title'] = 'Три.ч'
    params['threads'] = db_sess.query(Thread).order_by(desc(Thread.id))
    return render_template('home.html', **params)


# Страница где создаются, все треды

@app.route('/create_thread', methods=['GET', 'POST'])
def create_thread_page():
    form = ThreadCreateForm()
    if form.validate_on_submit():
        thread_title = form.title.data
        thread_theme = form.theme.data
        thread_main_text = form.text.data
        # Создаем запись в таблице posts
        post = Post()
        post.type = 'thread'
        post.created_date = datetime.now().date()
        post.created_time = datetime.now().time()
        db_sess = db_session.create_session()
        db_sess.add(post)
        db_sess.commit()
        # Собираем фотографии с формы
        images = []
        for file in [form.image_1.data, form.image_2.data,
                     form.image_3.data, form.image_4.data]:
            if file:
                filename = secure_filename(file.filename)
                filename = generate_s(9) + '.' + filename.split('.')[-1]
                filepath = 'static/images/' + filename
                file.save(filepath)
                image = Image()
                image.post_id = post.id
                image.title = filename
                image.file_path = filepath
                images.append(filepath)
                db_sess.add(image)
                db_sess.commit()
        # Создаем запись в таблице threads
        thread = Thread()
        thread.title = form_text(thread_title, 156)
        thread.post_id = post.id
        thread.theme = form_text(thread_theme, 156)
        thread.main_text = form_text(thread_main_text, 156)
        thread.images = images
        thread.answers_amount = 0
        thread.date = post.created_date.strftime("%d/%m/%Y")
        thread.time = post.created_time.strftime("%H.%M.%S")
        db_sess.add(thread)
        db_sess.commit()
        return redirect('/home')
    param = dict()
    param['title'] = 'Три.ч - Создание треда'
    param['form'] = form
    return render_template('create-thread.html', **param)


# На этой странице разваорачивается тред и все ответы к нему

@app.route('/thread/<int:post_id>', methods=['GET'])
def open_thread(post_id):
    db_sess = db_session.create_session()
    param = dict()
    param['title'] = f'Три.ч - Тред №{post_id}'
    param['threads'] = db_sess.query(Thread).filter(Thread.post_id == post_id)
    param['answers'] = db_sess.query(Answer).filter(Answer.thread_id == post_id)
    return render_template('thread-open.html', **param)


# Страница создания ответа к записи

@app.route('/answer/<int:post_id>', methods=['GET', 'POST'])
def answer_page(post_id):
    db_sess = db_session.create_session()
    answering_to = post_id
    response = db_sess.query(Post).filter(Post.id == answering_to)
    type_of_post = None
    for p in response:
        type_of_post = p.type
    form = AnswerForm()
    if form.validate_on_submit():
        answer_text = form.text.data
        # Заводим запись в таблице posts
        post = Post()
        post.type = 'answer'
        post.created_date = datetime.now().date()
        post.created_time = datetime.now().time()
        db_sess.add(post)
        db_sess.commit()
        # Бежим по фотографиям
        images = []
        for file in [form.image_1.data, form.image_2.data,
                     form.image_3.data, form.image_4.data]:
            if file:
                filename = secure_filename(file.filename)
                filename = generate_s(9) + '.' + filename.split('.')[-1]
                filepath = 'static/images/' + filename
                file.save(filepath)
                image = Image()
                image.post_id = post.id
                image.title = filename
                image.file_path = filepath
                images.append(filepath)
                db_sess.add(image)
                db_sess.commit()
        # Создаем запись об ответе
        answer = Answer()
        answer.main_text = form_text(answer_text, 176)
        answer.post_id = post.id
        answer.answering_to = answering_to
        answer.images = images
        answer.date = post.created_date.strftime("%d/%m/%Y")
        answer.time = post.created_time.strftime("%H.%M.%S")
        answer.thread_id = answering_to
        if type_of_post == 'thread':
            answer.thread_id = answering_to
            db_sess.add(answer)
            db_sess.commit()
            return redirect(f'/thread/{answering_to}')
        else:
            post = None
            for a in db_sess.query(Answer).filter(Answer.post_id == answering_to):
                post = a
            answer.thread_id = post.thread_id
            db_sess.add(answer)
            db_sess.commit()
            return redirect(f'/thread/{post.thread_id}')
    param = dict()
    param['title'] = f'Три.ч - Ответ №{answering_to}'
    param['post_type'] = type_of_post
    if type_of_post == 'thread':
        param['posts'] = db_sess.query(Thread).filter(Thread.post_id == answering_to)
    else:
        param['posts'] = db_sess.query(Answer).filter(Answer.post_id == answering_to)
    param['form'] = form
    return render_template('answer.html', **param)


def main():
    app.config['SECRET_KEY'] = generate_s(17)
    db_session.global_init("db/forum_content.db")
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    main()
