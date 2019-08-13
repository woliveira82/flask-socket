from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return open('views/index.html').read()


if __name__ == '__main__':
    app.run('127.0.0.1', '5000', debug=True)
