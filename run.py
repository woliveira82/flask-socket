from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/')
def hello():
    return render_template('index.html')


@socketio.on('message')
def messageReceive(data):
    emit('message', data, broadcast=True)


@socketio.on('enter')
def enterRoom(name):
    
    emit('notification', name + ' entrou na sala.', broadcast=True)


if __name__ == '__main__':
    socketio.run(app, '0.0.0.0', '5000')
