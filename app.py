from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_socketio import send, emit
from subprocess import call
import RPi.GPIO as gpio

#call(‘halt’, shell=False)
gpio.setmode(gpio.BOARD) # Ponemos la placa en modo BOARD
gpio.setup(4, gpio.IN) 


gpio.add_event_detect(4, gpio.RISING, callback=shutdown, bouncetime=200)
# Inici
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@socketio.on('my event')
def handle(json):
    emit('my response', json)
    print(json)


@app.route("/")
def index():
    return render_template("index.html")

def shutdown(pin):
    emit('my response', {data: pin})

if __name__ == '__main__':
    socketio.run(app)

