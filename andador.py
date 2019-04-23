#!/usr/bin/env python3
# coding: utf-8

import ev3dev.ev3 as ev3
from ev3dev.ev3 import *
from enum import Enum
#from multiprocessing import Process
from time import sleep
from time import time

class States(Enum):
    turnLeft = -1
    goForward = 0
    turnRight = 1
    sleep = 2


class Robot:
    def __init__(self,out1,out2,in1,in2):
        self.speed = speed
        self.time = time

        self.self.lm1 = ev3.LargeMotor(self.out1); assert self.lm1.connected
        self.self.lm2 = ev3.LargeMotor(self.out2); assert self.lm2.connected
        self.se = ev3.ColorSensor(self.in1); assert self.se.connected
        self.sd = ev3.ColorSensor(self.in2); assert self.sd.connected

    def turn_left(self,speed,time):
        self.lm1.run_timed(speed_sp = -speed, time_sp = time, stop_action = 'coast')
        self.lm2.run_timed(speed_sp = speed, time_sp = time, stop_action = 'coast')
    def turn_right(self,speed,time):
        self.lm1.run_timed(speed_sp = speed, time_sp = time, stop_action = 'coast')
        self.lm2.run_timed(speed_sp = -speed, time_sp = time, stop_action = 'coast')
    def go_forward(self,speed,time):
        self.lm1.run_timed(speed_sp = -1*speed, time_sp = time, stop_action = 'coast')
        self.lm2.run_timed(speed_sp = -1*speed, time_sp = time, stop_action = 'coast')
    def abrirAprendizado(self,color,txt):
        with open(self.txt, "r") as ft:            # a lista de aprendizado serah "azul, verde, vermelho"
            self.color = ft.read().split(',')              # aqui, criamos uma lista de strings, cada elemento eh a cor
            self.color.pop()
            for x in self.color:
                print("x", x, "int(x)", int(x))
            self.color = [int(x) for x in self.color]     # tornamos as strings em inteiros

    def verificaCor(self):
        # 1 preto e 0 branco
        left = self.se.raw()
        right = self.sd.raw()
        if branco[0]<=left[0] and branco[1]>=left[0] and branco[2]<=left[1] and branco[3]>=left[1] and branco[4]<=left[2] and branco[5]>=left[2]:
            left = 0
        elif preto[0]<=left[0] and preto[1]>=left[0] and preto[2]<=left[1] and preto[3]>=left[1] and preto[4]<=left[2] and preto[5]>=left[2]:
            left = 1
        if branco[0]<=right[0] and branco[1]>=right[0] and branco[2]<=right[1] and branco[3]>=right[1] and branco[4]<=right[2] and branco[5]>=right[2]:
            right = 0
        elif preto[0]<=right[0] and preto[1]>=right[0] and preto[2]<=right[1] and preto[3]>=right[1] and preto[4]<=right[2] and preto[5]>=right[2]:
            right = 1

    def verificaEstado(self):
        if left == 1 and right == 0:
            estado = States(-1)
        if left == 0 and right == 0:
            estado = States(0)
        if left == 0 and right == 1:
            estado = States(1)
        if left == 1 and right == 1:
            estado = States(2)

    def follow_line(self,speed_reta,speed_curva):
        while(True):
            Robot.verificaCor()
            Robot.verificaEstado()
            print(left, " ", right, " ", estado '\n')


            if(estado == States(0)): #white and white
                Robot.go_forward(self.speed_reta, 1)
                print(States(0))

            if(estado == States(2)): #black and black
                sleep(1)
                print(States(2))

            if(estado == States(-1)): #black and white
                sleep(0.1)
                while(not(left == 0 and left == 0)):
                    Robot.turn_left(self.speed_curva, 1)
                    print(left, " ", right, '\n')
                    print(States(-1))

            if(estado == States(1)): #white and black
                sleep(0.1)
                while(not (left == 0 and right == 0)):
                    Robot.turn_right(self.speed_curva, 1)
                    print(left, " ", right, '\n')
                    print(States(1))

Corsa = Robot('outA','outD','in2','in4')
Corsa.abrirAprendizado(branco,branco.txt)
Corsa.abrirAprendizado(preto,preto.txt)
Corsa.follow_line(400,800)
#obs.: testar curva com duas rodas girando (uma muito pouco), com uma parada e outra girando ou com uma para cada lado

