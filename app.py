from flask import Flask, render_template, session, request, jsonify, current_app, copy_current_request_context
from flask_socketio import SocketIO
from flask_socketio import send, emit
from flask_cors import CORS
from subprocess import call
import requests
import RPi.GPIO as gpio


verde=23
amarillo=18
rojo=25
entrada1=22
entrada2=21
entrada3=20
timbre=12
gpio.setmode(gpio.BCM)
gpio.setup(verde,gpio.OUT)
gpio.setup(amarillo,gpio.OUT)
gpio.setup(rojo,gpio.OUT)
gpio.setup(entrada1,gpio.IN)
gpio.setup(entrada2,gpio.IN)
gpio.setup(entrada3,gpio.IN)
gpio.setup(timbre,gpio.OUT)

"""
while True:
    try:
		if gpio.input(21):
			gpio.output(verde,True)
			sleep(0.5)
			gpio.output(verde,False)
            
            
    except  KeyboardInterrupt:
			gpio.cleanup()

"""
app = Flask(__name__)
cors = CORS(app)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
press_counter = 1

@socketio.on('connect', namespace='/')
def local_client_connect():
    pass
    
def shutdown(pin):
    print("cantidad de pulsaciones",pin)
        
def manejo(button_pressed):
    global press_counter
    press_counter += 1
    with app.test_request_context('/'):
        print(press_counter)
        socketio.emit('my response',{"data":press_counter}, namespace="/")
        print("soy el server y me llego",press_counter)

gpio.add_event_detect(21, gpio.RISING, callback = manejo, bouncetime=200)


@app.route("/")
def index():
    #emit('my response', {"data": "22"})
    return render_template("index.html")


if __name__ == '__main__':
    socketio.run(app)
    
    #app.run()




