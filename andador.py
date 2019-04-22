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

class LineFollower(Robot):
    def __init__(self):
        Robot.__init__(self)

    def abrirAprendizadoWhite():
    ## try: tenta abrir um arquivo de aprendizado
    try:
        with open("white_esq.txt", "r") as ft:            # a lista de aprendizado serah "azul, verde, vermelho"
            white = ft.read().split(',')              # aqui, criamos uma lista de strings, cada elemento eh a cor
            white.pop()
            for x in white:
                print("x", x, "int(x)", int(x))
            white = [int(x) for x in white]     # tornamos as strings em inteiros
    except:
        white = [47, 47, 47]                         # caso nao haja arquivo, criamos a lista

    def abrirAprendizadoBlack():
    ## try: tenta abrir um arquivo de aprendizado
    try:
        with open("black_esq.txt", "r") as ft:            # a lista de aprendizado serah "azul, verde, vermelho"
            black = ft.read().split(',')              # aqui, criamos uma lista de strings, cada elemento eh a cor
            black.pop()
            for x in black:
                print("x", x, "int(x)", int(x))
            black = [int(x) for x in black]     # tornamos as strings em inteiros
    except:
        black = [47, 47, 47]                         # caso nao haja arquivo, criamos a lista


    def sensorEsquerdo():
        for i in white:
            for j in esq:
                if (esq > white - 20 or esq < white + 20)
                    return 0

        for i in black:
            for j in esq:
                if (esq > black - 20 or esq < black + 20)
                    return 1

    def sensorDireito():
        for i in white:
            for j in dir:
                if (dir > white - 20 or dir < white + 20)
                    return 0

        for i in black:
            for j in dir:
                if (dir > black - 20 or dir < black + 20)
                    return 1


    def follow(self):
        #obs.: sem calibração, primeiro vamos testar com a leitura padrão do sensor
        esq = se.raw()
        esq = str(esq)
        dir = sd.raw()
        dir = str(dir)

        # 1 preto e 0 branco
        print(esq, " ", dir, '\n')
        if(LineFollower.sensorEsquerdo() == 0 and LineFollower.sensorDireito() == 0): #white and white
            Robot.go_forward(self, self.speed, 1)

        if(LineFollower.sensorEsquerdo() == 1 and LineFollower.sensorDireito() == 1): #black and black
            sleep(1)
        else:
            if(LineFollower.sensorEsquerdo() == 1 and LineFollower.sensorDireito() == 0): #black and white
                while(not(LineFollower.sensorEsquerdo() == 0 and LineFollower.sensorDireito() == 0)):
                    Robot.turn_left(self, self.speed, 1)
                    print(esq, " ", dir, '\n')
                    print("esquerda")
            if(LineFollower.sensorEsquerdo() == 0 and LineFollower.sensorDireito() == 1): #white and black
                while(not (LineFollower.sensorEsquerdo() == 0 and LineFollower.sensorDireito() == 0)):
                    Robot.turn_right(self, self.speed, 1)
                    print("direita")
                    print(esq, " ", dir, '\n')

#APLICAR CALIBRAÇÃO
Corsa = LineFollower()
Corsa.speed = 400
Corsa.time = 1000
Corsa.abrirAprendizadoWhite()
Corsa.abrirAPrendizadoBlack()
while(True):
    Corsa.follow()

