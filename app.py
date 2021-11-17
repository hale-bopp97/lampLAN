import RPi.GPIO as GPIO
from flask import Flask, render_template, request

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#define lamp actuator
lampGPIO = 17

#initialize GPIO status var
lampStats = 0

#Definelamp pin as output
GPIO.setup(lampGPIO, GPIO.OUT)

#turn lamp OFF
GPIO.output(lampGPIO, GPIO.HIGH)

@app.route('/')
def index():
    lampStats = GPIO.input(lampGPIO)

    templateData = {'lampGPIO' : lampStats}
    return render_template('index.html', **templateData)

@app.route('/<deviceName>/<action>')
def action(deviceName, action):
    if deviceName == 'lampGPIO':
        actuator = lampGPIO

    if action == 'on':
        GPIO.output(actuator, GPIO.LOW)
    if action == 'off':
        GPIO.output(actuator, GPIO.HIGH)

    lampStats = GPIO.input(lampGPIO)

    templateData = {'lampGPIO' : lampStats}
    return render_template('index.html', **templateData)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000, debug = True)
