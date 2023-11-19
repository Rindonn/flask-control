#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@ Author: Rindon
@ Date: 2023-11-07 09:24:26
LastEditors: Rindon
LastEditTime: 2023-11-18 13:39:25
@ Description: Remote control module of raspberry pi 4B by using python-flask
'''
import pi_Control
from flask import Flask
from flask import render_template
from flask import url_for
import time
from pi_Photo import pi_Photo 
import sys

app = Flask(__name__)
number = 0
#If flask server can't start,comment these two lines.
#Maybe pi can't connect to ftp server.
upload = pi_Photo()
upload.ftp_Link()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<control>')
def remote_Control(control):
    '''
        description:'Interface for remote control from web.',
        param:'control with (Left,Right,Forward,Backward)',
        return:'Back to the index page after 1 second.'
    '''
    if control == "Left":
        text = "Turn left!"
        pi_Control.turn_Left()
        time.sleep(0.25)
    elif control == "Right":
        text = "Turn right!"
        pi_Control.turn_Right()
        time.sleep(0.25)
    elif control == "Forward":
        text = "Move forward!"
        pi_Control.move_Forward()
        time.sleep(0.25)
    elif control == "Backward":
        pi_Control.move_Backward()
        text = "Move backward!"
        time.sleep(0.25)
    elif control == "Stop":
        upload.ftp_Close()
        print("Program stop!")
        pi_Control.stop()
        sys.exit()
    elif control == "Test":
        pi_Control.test_Control()
        text = "Test control!"
        time.sleep(0.25)
    else:
        pi_Control.stop()
        text = "Undefined param. Stop."
        time.sleep(0.25)
    
    return f'{text}<script>setTimeout(() => window.location.href = "{url_for("index")}", 1000)</script>'

@app.route('/server/<control>')
def server_Control(control):
    '''
        description:'Interface for remote control from server by using request library.
                    Move,stop and take a photo and upload to ftp server.',
        param:'control with (Left,Right,Forward,Backward)',
        return:'None'
    '''
    global number
    if control == "Left":
        text = "Turn left!"
        pi_Control.turn_Left()
        time.sleep(0.25)
        pi_Control.stop()
        upload.ftp_Upload(number,control)
        number = number + 1
    elif control == "Right":
        text = "Turn right!"
        pi_Control.turn_Right()
        time.sleep(0.25)
        pi_Control.stop()
        upload.ftp_Upload(number,control)
        number = number + 1
    elif control == "Forward":
        text = "Move forward!"
        pi_Control.move_Forward()
        time.sleep(0.25)
        pi_Control.stop()
        upload.ftp_Upload(number,control)
        number = number + 1
    elif control == "Backward":
        pi_Control.move_Backward()
        text = "Move backward!"
        time.sleep(0.25)
        pi_Control.stop()
        upload.ftp_Upload(number,control)
        number = number + 1
    elif control == "STOP":
        upload.ftp_Close()
        print("Program stop")
        pi_Control.stop()
        #Still don't know how close flask from python.
    else:
        pi_Control.stop()
        text = "Undefined param. Stop."
        time.sleep(0.25)
    return text

if __name__ == "__main__":
    #Start flask server from here
    app.run(host="0.0.0.0",port=8000,debug=True)
