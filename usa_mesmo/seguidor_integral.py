#!/usr/bin/env python3
# coding: utf-8
import ev3dev.ev3 as ev3
from ev3dev.ev3 import *
from enum import Enum
#from multiprocessing import Process
from time import sleep
from time import time

class States(Enum):
    Esquerda = -1
    Reto = 0
    Direita = 1

class Robot:
    def __init__(self,out1,out2,in1,in2,in3):

        self.lm1 = ev3.LargeMotor(out1); assert self.lm1.connected
        self.lm2 = ev3.LargeMotor(out2); assert self.lm2.connected
        self.se = ev3.ColorSensor(in1); assert self.se.connected
        self.sm = ev3.ColorSensor(in2); assert self.sm.connected
        self.sd = ev3.ColorSensor(in3); assert self.sd.connected
        #self.su = ev3.UltrasonicSensor(in4); assert self.su.connected


    def verificaIntensidade(self):
        global esquerdo
        global meio
        global direito
        global target
        global trigger
        global turn
        global errorLeft
        global errorRight
        global kp
        global correctionLeft
        global correctionRight
        global integralLeft
        global integralRight
        global derivativeLeft
        global derivativeRight
        global lastErrorLeft
        global lastErrorRight
        global ki
        global kd
        left = self.se.reflected_light_intensity
        middle = self.sm.reflected_light_intensity
        right = self.sd.reflected_light_intensity

        errorLeft = left - target
        errorRight = right - target
        integralLeft += errorLeft
        integralRight += errorRight
        derivativeLeft = errorLeft - lastErrorLeft
        derivativeRight = errorRight - lastErrorRight
        correctionLeft = errorLeft * kp + integralLeft * ki + derivativeLeft * kd
        correctionRight = errorRight * kp + integralRight * ki + derivativeRight * kd

        lastErrorLeft = errorLeft
        lastErrorRight = errorRight
        #correciton = (error * kp) + (integral * ki) + (derivative * kd)
        #error = target - value
        #integral = integral + error
        #derivative = error - last_error

    def seguidor(self,initialSpeed):
        self.lm1.run_forever(speed_sp = -(initialSpeed + correctionLeft))
        self.lm2.run_forever(speed_sp = -(initialSpeed + correctionRight))

    def seguirLinha(self,speed_reta,speed_curva):
        global esquerdo
        global meio
        global direito
        while(True):
            Robot.verificaIntensidade(self)
            Robot.seguidor(self,speed_reta)


turn = 0
esquerdo = 0
direito = 0
meio = 0
trigger = 28
kp = 10
ki = -0.01
kd = 1
target = 50
errorLeft = 0
errorRight = 0
correctionLeft = 0
correcitonRight = 0
integralLeft = 0
integralRight = 0
derivativeLeft = 0
derivativeRight = 0
lastErrorLeft = 0
lastErrorRight = 0

#with open('estados.txt', "w") as arquivo:
#    arquivo.write("BEGIN")

Corsa = Robot('outB','outD','in2','in3','in4')
Sound.speak('Hello, I am Corsa')
Corsa.seguirLinha(200,90)
