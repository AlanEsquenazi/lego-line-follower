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

while(True):
    LineFollower.follow(800)

