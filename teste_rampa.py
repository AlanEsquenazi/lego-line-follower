#!/usr/bin/env python3
# coding: utf-8

import ev3dev.ev3 as ev3
#from multiprocessing import Process
from time import sleep
from time import time

lm1 = ev3.LargeMotor('outD')
lm2 = ev3.LargeMotor('outA')

while(True):
    lm1.run_timed(speed_sp = -400, time_sp = 10000, stop_action = 'coast')
    lm2.run_timed(speed_sp = -400, time_sp = 10000, stop_action = 'coast')
