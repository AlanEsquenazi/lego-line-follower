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
    def __init__(self):

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
        self.esq_lida = se.raw
        self.esq_lida = str(esq_lida)
        white_esq.write(esq_lida);

        with open("white_dir.txt", "w") as white_dir:
        dir_lida = sd.raw
        dir_lida = str(dir_lida)
        white_dir.write(dir_lida);

class LineFollower(Robot):
    def __init__(self):
        Robot.__init__(self)

    def follow(self,speed):
        #obs.: sem calibração, primeiro vamos testar com a leitura padrão do sensor
        self.esq = se.value()
        self.dir = sd.value()
        if(self.esq == 6 and self.dir == 6): #white and white
            Robot.go_forward(speed,1)
            #precisa do Robot. ?
        if(self.esq == 1 and self.dir == 6): #black and white
            Robot.turn_left(speed,1)
        if(self.esq == 6 and self.dir == 1): #white and black
            Robot.turn_right(speed,1)
        if(self.esq == 1 and self.dir == 1): #black and black
            sleep(1)

Calibration.white()

while(True):

    LineFollower.follow(800)

