from flask_socketio import emit, send

from app import socketio


@socketio.on('message')
def messageReceive(data):
    emit('message', data, broadcast=True)


@socketio.on('enter')
def enterRoom(name):
    emit('notification', name + ' entrou na sala.', broadcast=True)
