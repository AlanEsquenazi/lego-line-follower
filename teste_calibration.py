#!/usr/bin/env python
# coding: utf-8
import ev3dev.ev3 as ev3
from ev3dev.ev3 import *
#from multiprocessing import Process
from time import sleep
from time import time
se = ev3.ColorSensor('in2'); assert se.connected

class Robot:
    def __init__(self,color,txt):
        self.speed = 0
        self.time = 0
        self.color = color
        self.txt = txt
    def turn_left(self,speed,time):
        lm1.run_timed(speed_sp = -speed, time_sp = time, stop_action = 'coast')
        lm2.run_timed(speed_sp = speed, time_sp = time, stop_action = 'coast')
    def turn_right(self,speed,time):
        lm1.run_timed(speed_sp = speed, time_sp = time, stop_action = 'coast')
        lm2.run_timed(speed_sp = -speed, time_sp = time, stop_action = 'coast')
    def go_forward(self,speed,time):
        lm1.run_timed(speed_sp = -1*speed, time_sp = time, stop_action = 'coast')
        lm2.run_timed(speed_sp = -1*speed, time_sp = time, stop_action = 'coast')

    def abrirAprendizado(self):
        with open(txt, "r") as ft:            # a lista de aprendizado serah "azul, verde, vermelho"
            self.color = ft.read().split(',')              # aqui, criamos uma lista de strings, cada elemento eh a cor
            for x in self.color:
                print("x", x, "int(x)", int(x))
            self.color = [int(x) for x in self.color]     # tornamos as strings em inteiros

    def verificaCor():
        esq = se.raw()
        if branco[0]<=esq[0] and branco[1]>=esq[0] and branco[2]<=esq[1] and branco[3]>=esq[1] and branco[4]<=esq[2] and branco[5]>=esq[2]:
            esq = 0
            print("BRANCO/WHITE/BLANC")
        elif preto[0]<=esq[0] and preto[1]>=esq[0] and preto[2]<=esq[1] and preto[3]>=esq[1] and preto[4]<=esq[2] and preto[5]>=esq[2]:
            esq = 1
            print("PRETO/BLACK/NOIR")
branco = [0,0,0,0,0,0]
preto = [0,0,0,0,0,0]
Branco = Robot(branco,branco.txt)
Preto = Robot(preto,preto.txt)
Branco.abrirAprendizado()
Preto.abrirAprendizado()
while(True):
    Branco.verificaCor()



