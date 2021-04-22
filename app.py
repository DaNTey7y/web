from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    param = dict()
    param['title'] = 'Три.ч'
    return render_template('home.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
