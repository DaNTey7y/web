from flask import Flask, render_template
from data import db_session

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    param = dict()
    param['title'] = 'Три.ч'
    return render_template('home.html', **param)


def main():
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()
