#!/usr/bin/env python3
# coding: utf-8
import ev3dev.ev3 as ev3
from ev3dev.ev3 import *
from enum import Enum
#from multiprocessing import Process
from time import sleep
from time import time

class Robot:
    def __init__(self,out1,out2,in1,in2):

        self.lm1 = ev3.LargeMotor(out1); assert self.lm1.connected
        self.lm2 = ev3.LargeMotor(out2); assert self.lm2.connected
        self.us = ev3.UltrasonicSensor(in4); assert self.us.connected

    def stop(self,time):
        self.lm1.run_timed(speed_sp = 0, time_sp = time, stop_action = 'coast')
        self.lm2.run_timed(speed_sp = 0, time_sp = time, stop_action = 'coast')

    def turn_left(self,speed,time):
        self.lm1.run_timed(speed_sp = speed, time_sp = time, stop_action = 'coast')
        self.lm2.run_timed(speed_sp = -speed, time_sp = time, stop_action = 'coast')

    def turn_right(self,speed,time):
        self.lm1.run_timed(speed_sp = -speed, time_sp = time, stop_action = 'coast')
        self.lm2.run_timed(speed_sp = speed, time_sp = time, stop_action = 'coast')

    def go_forward(self,speed,time):
        self.lm1.run_timed(speed_sp = -speed, time_sp = time, stop_action = 'coast')
        self.lm2.run_timed(speed_sp = -speed, time_sp = time, stop_action = 'coast')
    def desvia_do_obstaculo(self, speed,time):
        Robot.turn_right(self,speed,time)
        Robot.go_forward(self,speed,time)
        Robot.turn_left(self,speed,time)
        Robot.go_forward(self,speed,time)
        Robot.turn_left(self,speed,time)
        Robot.go_forward(self,speed,time)
        Robot.turn_right(self,speed,time)

    def encontrar_obstaculo(self):
        self.us.mode = 'US_DIST_CM'
        if(us.value()<=50):
            Robot.desvia_do_obstaculo(self)






