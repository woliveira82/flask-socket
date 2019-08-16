from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/')
def hello():
    return open('views/index.html').read()


@socketio.on('message')
def messageReceive(data):
    print(data)
    emit('message', data, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, '0.0.0.0', '5000')
