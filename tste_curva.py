#!/usr/bin/env python3
# coding: utf-8

import ev3dev.ev3 as ev3
from ev3dev.ev3 import *
#from multiprocessing import Process
from time import sleep
from time import time

lm1 = ev3.LargeMotor('outD'); assert lm1.connected
lm2 = ev3.LargeMotor('outA'); assert lm2.connected

class Robot:
    def __init__(self):
        self.speed = 0
        self.time = 0
    def turn_left(self,speed,time):
        print('esquerda')
        lm1.run_timed(speed_sp = -speed, time_sp = time, stop_action = 'coast')
        lm2.run_timed(speed_sp = speed, time_sp = time, stop_action = 'coast')
    def turn_right(self,speed,time):
        print('direita')
        lm1.run_timed(speed_sp = speed, time_sp = time, stop_action = 'coast')
        lm2.run_timed(speed_sp = -speed, time_sp = time, stop_action = 'coast')
    def go_forward(self,speed,time):
        lm1.run_timed(speed_sp = -1*speed, time_sp = time, stop_action = 'coast')
        lm2.run_timed(speed_sp = -1*speed, time_sp = time, stop_action = 'coast')
corsinha = Robot()
corsinha.speed = 400
corsinha.time = 1000
while 1:
    print("TURN1")
    corsinha.turn_left(400, 1000)
    print("TURN2")
    corsinha.turn_right(400, 1000)