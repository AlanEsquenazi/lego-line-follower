#!/usr/bin/env python3
# coding: utf-8

import ev3dev.ev3 as ev3
from ev3dev.ev3 import *
#from multiprocessing import Process
from time import sleep
from time import time

lm1 = ev3.LargeMotor('outD'); assert lm1.connected
lm2 = ev3.LargeMotor('outA'); assert lm2.connected

se = ev3.ColorSensor('in1'); assert se.connected
sd = ev3.ColorSensor('in4'); assert sd.connected
while(True):
    esq = se.value()
    dir = sd.value()
    if(se == 6 and sd == 6): #white and white
        #go forward
        lm1.run_timed(speed_sp = 800, time_sp = 100, stop_action = 'coast')
        lm2.run_timed(speed_sp = 800, time_sp = 100, stop_action = 'coast')
    if(se == 1 and sd == 6): #black and white
        #turn left
        lm1.run_timed(speed_sp = -800, time_sp = 1, stop_action = 'coast')
        lm2.run_timed(speed_sp = 800, time_sp = 1, stop_action = 'coast')
    if(se == 6 and sd == 1): #white and black
        #turn right
        lm1.run_timed(speed_sp = 800, time_sp = 1, stop_action = 'coast')
        lm2.run_timed(speed_sp = -800, time_sp = 1, stop_action = 'coast')
    if(se == 1 and sd == 1): #black and black
        #stop
        sleep(1)
