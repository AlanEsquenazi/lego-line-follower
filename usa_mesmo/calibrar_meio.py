#!/usr/bin/env python3
# coding: utf-8
import ev3dev.ev3 as ev3
from ev3dev.ev3 import *
#from multiprocessing import Process
from time import sleep
from time import time
lm1 = ev3.LargeMotor('outA'); assert lm1.connected
lm2 = ev3.LargeMotor('outC'); assert lm2.connected

cor = ev3.ColorSensor('in3'); assert cor.connected
class Calibracao:
    def __init__(self, color, speed, time):
        self.color = color
        self.speed = speed
        self.time = time
        self.p1 = [1021,-1]
        self.p2 = [1021,-1]
        self.p3 = [1021,-1]
    def calibrate(self, speed,time, wait_time, repeat):
        for i in range(repeat):
            lm1.run_timed(speed_sp = -1*speed, time_sp = time, stop_action = 'coast')
            lm2.run_timed(speed_sp = -1*speed, time_sp = time, stop_action = 'coast')
            sleep(wait_time)
            cor_lida = cor.raw
            self.p1[0] = min(cor.raw[0], self.p1[0])
            self.p1[1] = max(cor.raw[0], self.p1[1])
            self.p2[0] = min(cor.raw[1], self.p2[0])
            self.p2[1] = max(cor.raw[1], self.p2[1])
            self.p3[0] = min(cor.raw[2], self.p3[0])
            self.p3[1] = max(cor.raw[2], self.p3[1])
    def escrever(self):
        with open(self.color, "w") as arquivo:
            arquivo.write(str(self.p1[0]))
            arquivo.write(",")
            arquivo.write(str(self.p1[1]))
            arquivo.write(",")
            arquivo.write(str(self.p2[0]))
            arquivo.write(",")
            arquivo.write(str(self.p2[1]))
            arquivo.write(",")
            arquivo.write(str(self.p3[0]))
            arquivo.write(",")
            arquivo.write(str(self.p3[1]))
            arquivo.write(",")
branco = Calibracao("branco_meio.txt", 400, 10)
branco.calibrate(400, 10, 0, 100)
branco.escrever()
print("Calibrar preto")
Sound.speak("Calibrar preto")
sleep(10)
print("agora")
Sound.speak("Agora")
preto = Calibracao("preto_meio.txt",0,0)
preto.calibrate(0,0,0.1, 100)
preto.escrever()


