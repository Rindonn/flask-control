#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
LastEditors: Rindon
LastEditTime: 2023-11-18 13:25:38
@ Description: Add test function for testing availability
'''

import RPi.GPIO as GPIO
import time

AIN1 = 10
AIN2 = 9
BIN1 = 25
BIN2 = 11

GPIO.setmode(GPIO.BCM)     # set mode
GPIO.setwarnings(False)    # do not show warning msg

GPIO.setup(AIN1, GPIO.OUT)  # motor's input AIN 1(right motor) 
GPIO.setup(AIN2, GPIO.OUT)  # motor's input AIN 2(right motor) 
GPIO.setup(BIN1, GPIO.OUT)  # motor's input BIN 1(left motor) 
GPIO.setup(BIN2, GPIO.OUT)  # motor's input BIN 2(letf motor)

# move_forward
def move_Forward():
    GPIO.output(AIN2, GPIO.HIGH)
    GPIO.output(BIN1, GPIO.HIGH)
    # time.sleep(5)

# move_backward
def move_Backward():
    GPIO.output(AIN1, GPIO.HIGH)
    GPIO.output(BIN2, GPIO.HIGH)

# turn_left
def turn_Left():
    GPIO.output(BIN1, GPIO.HIGH)

# turn_right
def turn_Right():
    GPIO.output(AIN2, GPIO.HIGH)
    
# car stop
def stop():
    GPIO.output(AIN1, GPIO.LOW)
    GPIO.output(AIN2, GPIO.LOW)
    GPIO.output(BIN1, GPIO.LOW)
    GPIO.output(BIN2, GPIO.LOW)
    
# clean_GPIO
def clean_GPIO():
    GPIO.cleanup()

def test_Control():
    '''
        description:'Check the piTank by doing all the actions.',
        param:'None',
        return:'None.'
    '''
    move_Forward()
    time.sleep(0.2)
    print('forward')
    stop()
    time.sleep(0.5)
    move_Backward()
    time.sleep(0.2)
    print('backward')
    stop()
    time.sleep(0.5)
    turn_Left()
    time.sleep(0.2)
    print('left')
    stop()
    time.sleep(0.5)
    turn_Right()
    time.sleep(0.2)
    print('right')
    stop()

if __name__ == '__main__':
    #pi drive test
    test_Control()
    clean_GPIO()
