#!/usr/bin/env python3
# coding: utf-8
import ev3dev.ev3 as ev3
from ev3dev.ev3 import *
#from multiprocessing import Process
from time import sleep
from time import time
lm1 = ev3.LargeMotor('outD'); assert lm1.connected
lm2 = ev3.LargeMotor('outA'); assert lm2.connected

cor = ev3.ColorSensor('in1'); assert cor.connected
class Calibracao_andando:
    def __init__(self, color, speed, time):
        self.color = color
        self.speed = speed
        self.time = time
        self.p1 = [1021,-1]
        self.p2 = [1021,-1]
        self.p3 = [1021,-1]
    def calibrate(self, speed,time):
        for i in range(100):
            lm1.run_timed(speed_sp = -1*speed, time_sp = time, stop_action = 'coast')
            lm2.run_timed(speed_sp = -1*speed, time_sp = time, stop_action = 'coast')
            cor_lida = cor.raw
            self.p1[0] = min(cor.raw[0], self.p1[0])
            self.p1[1] = max(cor.raw[0], self.p1[1])
            self.p2[0] = min(cor.raw[1], self.p2[0])
            self.p2[1] = max(cor.raw[1], self.p2[1])
            self.p3[0] = min(cor.raw[2], self.p3[0])
            self.p3[1] = max(cor.raw[2], self.p3[1])
class Calibracao_parado:
    def __init__(self, color):
        self.color = color
        self.p1 = [1021,-1]
        self.p2 = [1021,-1]
        self.p3 = [1021,-1]
    def calibrate(self):
        for i in range(10):
            sleep(1000)
            cor_lida = cor.raw
            self.p1[0] = min(cor.raw[0], self.p1[0])
            self.p1[1] = max(cor.raw[0], self.p1[1])
            self.p2[0] = min(cor.raw[1], self.p2[0])
            self.p2[1] = max(cor.raw[1], self.p2[1])
            self.p3[0] = min(cor.raw[2], self.p3[0])
            self.p3[1] = max(cor.raw[2], self.p3[1])https://www.w3schools.com/python/python_for_loops.asp
    def escrever(self):
        with open(self.color, "w") as arquivo:
            arquivo.write(p1)
            arquivo.write("\n")
            arquivo.write(p2)
            arquivo.write("\n") 
            arquivo.write(p3)
            arquivo.write("\n")  
branco = Calibracao_andando("branco.txt", 400, 10)
branco.calibrate(400, 10)
branco.escrever()
sleep(10000)
preto = Calibracao_parado("preto.txt")
preto.calibrate()
preto.escrever()