from flask import render_template
from flask_socketio import emit, send


@socketio.on('message')
def handle_message(message):
    send(message)


@socketio.on('json')
def handle_json(json):
    send(json, json=True)


@socketio.on('my event')
def handle_my_custom_event(json):
    emit('my response', json)


@app.route('/')
def index():
    print('index')
    return render_template('html/index.html')
    # return open("index.html").read()
