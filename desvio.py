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
        #self.od = ev3.ColorSensor(in1); assert self.se.connected
        #self.om = ev3.ColorSensor(in2); assert self.sm.connected

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

    def desviar(self,minimo1,minimo2):
        if(om.distancia <= minimo1):
            #para
            Robot.stop(self,1000)
            #vira até achar o obstáculo com o sensor direito
            while(not(od.distancia <= minimo1)):
                Robot.turn_left(self,600,60)

            while(not(estado == States(3)):
                Robot.turn_right(self,?,?) #Fazer curva com raio mt longo até encontrar a reta dnv






