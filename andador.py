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

class Robot:
    def turn_left(self,speed,time):
        lm1.run_timed(speed_sp = -speed, time_sp = time, stop_action = 'coast')
        lm2.run_timed(speed_sp = speed, time_sp = time, stop_action = 'coast')
    def turn_right(self,speed,time):
        lm1.run_timed(speed_sp = speed, time_sp = time, stop_action = 'coast')
        lm2.run_timed(speed_sp = -speed, time_sp = time, stop_action = 'coast')
    def go_forward(self,speed,time):
        lm1.run_timed(speed_sp = speed, time_sp = time, stop_action = 'coast')
        lm2.run_timed(speed_sp = speed, time_sp = time, stop_action = 'coast')

class Calibration(Robot):
    def __init__(self):
        Robot.__init__(self)

    def white():
        with open("white_esq.txt", "w") as white_esq:
            esq_lida = se.raw
            esq_lida = str(esq_lida)
            white_esq.write(esq_lida);

        with open("white_dir.txt", "w") as white_dir:
            dir_lida = sd.raw
            dir_lida = str(dir_lida)
            white_dir.write(dir_lida);

    def black():
        with open("black_esq.txt", "w") as black_esq:
            esq_lida = se.raw
            esq_lida = str(esq_lida)
            black_esq.write(esq_lida);

        with open("black_dir.txt", "w") as black_dir:
            dir_lida = sd.raw
            dir_lida = str(dir_lida)
            black_dir.write(dir_lida);

class LineFollower(Robot):
    def __init__(self):
        Robot.__init__(self)

    def follow(speed):
        #obs.: sem calibração, primeiro vamos testar com a leitura padrão do sensor
        esq = se.value()
        dir = sd.value()
        if(esq == 6 and dir == 6): #white and white
            go_forward(speed,1)
        if(esq == 1 and dir == 6): #black and white
            turn_left(speed,1)
        if(esq == 6 and dir == 1): #white and black
            turn_right(speed,1)
        if(esq == 1 and dir == 1): #black and black
            sleep(1)

Calibration.white()
Calibration.black()
while(True):
    LineFollower.follow(800)

