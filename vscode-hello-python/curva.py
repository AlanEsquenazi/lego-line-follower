#!/usr/bin/env python3
# coding: utf-8

import ev3dev.ev3 as ev3
#from multiprocessing import Process
from time import sleep
from time import time

lm1 = ev3.LargeMotor('outA')
lm2 = ev3.LargeMotor('outB')
#steer_pair = ev3.MoveSteering('outA', 'outB', motor_class=LargeMotor)
#anda pra frente
lm1.run_timed(speed_sp = 600, time_sp = 3000, stop_action = 'coast')
lm2.run_timed(speed_sp = 600, time_sp = 3000, stop_action = 'coast')
sleep(1)
#vira pra direita
lm2.run_timed(speed_sp = 600, time_sp = 600, stop_action = 'coast')
lm1.run_timed(speed_sp = -600, time_sp = 600, stop_action = 'coast')
sleep(1)
#anda pra
lm1.run_timed(speed_sp = 600, time_sp = 3000, stop_action = 'coast')
lm2.run_timed(speed_sp = 600, time_sp = 3000, stop_action = 'coast')
'''
#anda pra frente
#steer_pair.on_for_seconds(steering=0, speed=50, seconds=2)
lm1.on_for_seconds(speed = 60, seconds = 3)
lm2.on_for_seconds(speed = 60, seconds = 3)
sleep(1)
#anda pra direita
#steer_pair.on_for_seconds(steering=100, speed=50, seconds=1)
lm1.on_for_seconds(speed = -60, seconds = 2)
lm2.on_for_seconds(speed = 60, seconds = 2)
sleep(1)
#anda pra frente
#steer_pair.on_for_seconds(steering=0, speed=50, seconds=3)
lm1.on_for_seconds(speed = 60, seconds = 3)
lm2.on_for_seconds(speed = 60, seconds = 3)
sleep(1)
'''
