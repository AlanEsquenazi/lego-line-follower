#!/usr/bin/env python3
# coding: utf-8

import ev3dev.ev3 as ev3
from ev3dev.ev3 import *
#from multiprocessing import Process
from time import sleep
from time import time

lm1 = ev3.LargeMotor('outD'); assert lm1.connected
lm2 = ev3.LargeMotor('outA'); assert lm2.connected

se = ev3.ColorSensor('in2'); assert se.connected
sd = ev3.ColorSensor('in4'); assert sd.connected

class Robot:
    def __init__(self):
        self.speed = 0
        self.time = 0
    def turn_left(self,speed,time):
        lm1.run_timed(speed_sp = -speed, time_sp = time, stop_action = 'coast')
        lm2.run_timed(speed_sp = speed, time_sp = time, stop_action = 'coast')
    def turn_right(self,speed,time):
        lm1.run_timed(speed_sp = speed, time_sp = time, stop_action = 'coast')
        lm2.run_timed(speed_sp = -speed, time_sp = time, stop_action = 'coast')
    def go_forward(self,speed,time):
        lm1.run_timed(speed_sp = -1*speed, time_sp = time, stop_action = 'coast')
        lm2.run_timed(speed_sp = -1*speed, time_sp = time, stop_action = 'coast')
    def receive_white(self):
        with open("branco.txt", "r") as branco:
            lims_branco = branco.read.split(",")
        for i in range(6):
            lims_branco[i] = int(lims_branco[i])
    def receive_black(self):
        with open("preto.txt", "r") as preto:
            lims_preto = preto.read.split(",")
        for i in range(6):
            lims_preto[i] = int(lims_branco[i])
    def follow_line(self):
        esq = se.raw()
        direito = sd.raw()
        if lims_branco[0]<=esq[0] and lims_branco[1]>=esq[0] and lims_branco[2]<=esq[1] and lims_branco[3]>=esq[1] and lims_branco[4]<=esq[2] and lims_branco[5]>=esq[2]:
            esq = 0
        elif lims_preto[0]<=esq[0] and lims_preto[1]>=esq[0] and lims_preto[2]<=esq[1] and lims_preto[3]>=esq[1] and lims_preto[4]<=esq[2] and lims_preto[5]>=esq[2]:
            esq = 1
        if lims_branco[0]<=direito[0] and lims_branco[1]>=direito[0] and lims_branco[2]<=direito[1] and lims_branco[3]>=direito[1] and lims_branco[4]<=direito[2] and lims_branco[5]>=direito[2]:
            direito = 0
        elif lims_preto[0]<=direito[0] and lims_preto[1]>=direito[0] and lims_preto[2]<=direito[1] and lims_preto[3]>=direito[1] and lims_preto[4]<=direito[2] and lims_preto[5]>=direito[2]:
            direito = 1
        # 1 preto e 0 branco
        print(esq, " ", direito, '\n')
        if(esq == 0 and direito() == 0): #white and white
            Robot.go_forward(self, self.speed, 1)

        if(esq == 1 and direito == 1): #black and black
            sleep(1)
        else:
            if(esq == 1 and direito == 0): #black and white
                while(not(esq == 0 and esq == 0)):
                    Robot.turn_left(self, self.speed, 1)
                    print(esq, " ", direito, '\n')
                    print("esquerda")
            if(esq == 0 and direito == 1): #white and black
                while(not (esq == 0 and direito == 0)):
                    Robot.turn_right(self, self.speed, 1)
                    print("direita")
                    print(esq, " ", direito, '\n')

#APLICAR CALIBRAÇÃO
Corsa = LineFollower()
Corsa.speed = 400
Corsa.time = 1000
Corsa.receive_white()
Corsa.receive_black()
while(True):
    Corsa.follow_line()

