from flask import Flask, render_template, redirect
from random import choice
from datetime import datetime
from data import db_session
from data.posts import Post
from data.threads import Thread
from thread_create import ThreadCreateForm

app = Flask(__name__)


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home_page():
    return render_template('home.html', title='Три.ч')


@app.route('/create_thread', methods=['GET', 'POST'])
def create_thread_page():
    form = ThreadCreateForm()
    if form.validate_on_submit():
        images = []
        for f in [form.image_1.data, form.image_2.data,
                  form.image_3.data, form.image_4.data]:
            if f != '':
                images.append(f)
        thread_title = form.title.data
        thread_theme = form.theme.data
        thread_main_text = form.text.data
        post = Post()
        post.type = 'thread'
        post.created_date = datetime.now().date()
        post.created_time = datetime.now().time()
        db_sess = db_session.create_session()
        db_sess.add(post)
        db_sess.commit()
        thread = Thread()
        thread.title = thread_title
        thread.post_id = post.id
        thread.theme = thread_theme
        thread.images_amount = len(images)
        thread.main_text = thread_main_text
        thread.answers_amount = 0
        db_sess.add(thread)
        db_sess.commit()
        return redirect('/home')
    param = dict()
    param['title'] = 'Три.ч - Создание треда'
    param['form'] = form
    return render_template('create-thread.html', **param)


def main():
    symbs = 'abcdefghijklmnopqrstuvwxyz0123456789'
    key = ''.join([choice(symbs) for i in range(21)])
    app.config['SECRET_KEY'] = key
    db_session.global_init("db/forum_content.db")
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()
