#!/usr/bin/env python3
# coding: utf-8
import ev3dev.ev3 as ev3
from ev3dev.ev3 import *
from enum import Enum
#from multiprocessing import Process
from time import sleep
from time import time

lm1 = ev3.LargeMotor('outB'); assert lm1.connected
lm2 = ev3.Large4Motor('outD'); assert lm2.connected


'''def stop(time):
    lm1.run_timed(speed_sp = 0, time_sp = time, stop_action = 'coast')
    lm2.run_timed(speed_sp = 0, time_sp = time, stop_action = 'coast')

def curva_esquerda(speed,time):
    while(True):
        lm1.run_timed(speed_sp = speed, time_sp = time, stop_action = 'coast')
        lm2.run_timed(speed_sp = 0, time_sp = time, stop_action = 'coast')


curva_esquerda(600,60)'''

lm1.run_to_rel_pos(position_sp = 1000)
lm2.run_to_rel_pos(position_sp = 1000)


