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


        self.lm1 = ev3.LargeMotor(out1); assert self.lm1.connected
        self.lm2 = ev3.LargeMotor(out2); assert self.lm2.connected
        self.se = ev3.ColorSensor(in1); assert self.se.connected
        self.sd = ev3.ColorSensor(in2); assert self.sd.connected

    def turn_left(self,speed,time):
        self.lm1.run_timed(speed_sp = speed, time_sp = time, stop_action = 'coast')
        self.lm2.run_timed(speed_sp = -speed, time_sp = time, stop_action = 'coast')
    def turn_right(self,speed,time):
        self.lm1.run_timed(speed_sp = -speed, time_sp = time, stop_action = 'coast')
        self.lm2.run_timed(speed_sp = speed, time_sp = time, stop_action = 'coast')
    def go_forward(self,speed,time):
        self.lm1.run_timed(speed_sp = -1*speed, time_sp = time, stop_action = 'coast')
        self.lm2.run_timed(speed_sp = -1*speed, time_sp = time, stop_action = 'coast')
    def abrirAprendizadoBranco(self):
        global branco
        with open('branco.txt', "r") as ft:            # a lista de aprendizado serah "azul, verde, vermelho"
            branco = ft.read().split(',')              # aqui, criamos uma lista de strings, cada elemento eh a cor
            branco.pop()
            branco = [int(x) for x in branco]     # tornamos as strings em inteiros

    def abrirAprendizadoPreto(self):
        global preto
        with open('preto.txt', "r") as ft:            # a lista de aprendizado serah "azul, verde, vermelho"
            preto = ft.read().split(',')              # aqui, criamos uma lista de strings, cada elemento eh a cor
            preto.pop()
            preto = [int(x) for x in preto]     # tornamos as strings em inteiros

    def verificaCor(self):
        # 1 preto e 0 branco
        global left
        global right
        global esquerdo
        global direito
        left = self.se.raw
        right = self.sd.raw
        if branco[0]<=left[0] and branco[1]>=left[0] and branco[2]<=left[1] and branco[3]>=left[1] and branco[4]<=left[2] and branco[5]>=left[2]:
            esquerdo = 0
        elif preto[0]<=left[0] and preto[1]>=left[0] and preto[2]<=left[1] and preto[3]>=left[1] and preto[4]<=left[2] and preto[5]>=left[2]:
            esquerdo = 1
        if branco[0]<=right[0] and branco[1]>=right[0] and branco[2]<=right[1] and branco[3]>=right[1] and branco[4]<=right[2] and branco[5]>=right[2]:
            direito = 0
        elif preto[0]<=right[0] and preto[1]>=right[0] and preto[2]<=right[1] and preto[3]>=right[1] and preto[4]<=right[2] and preto[5]>=right[2]:
            direito = 1

    def verificaEstado(self):
        global esquerdo
        global direito
        global estado
        if esquerdo == 1 and direito == 0:
            estado = States(-1)
        elif esquerdo == 0 and direito == 0:
            estado = States(0)
        if esquerdo == 0 and direito == 1:
            estado = States(1)
        elif esquerdo == 1 and direito == 1:
            estado = States(2)

    def follow_line(self,speed_reta,speed_curva):
        while(True):
            global left
            global right
            global esquerdo
            global direito
            global estado
            Robot.verificaCor(self)
            Robot.verificaEstado(self)
            print(esquerdo, " ", direito, " ", estado)


            if(estado == States(0)): #white and white
                Robot.go_forward(self,speed_reta, 1)

            if(estado == States(2)): #black and black
                sleep(1)

            if(estado == States(-1)): #black and white
                sleep(0.5)
                while(not(estado == States(0))):
                    Robot.verificaCor(self)
                    Robot.verificaEstado(self)
                    Robot.turn_left(self,speed_curva, 1)
                    print(esquerdo, " ", direito, " ", estado)
            if(estado == States(1)): #white and black
                sleep(0.5)
                while(not (estado == States(0))):
                    Robot.verificaCor(self)
                    Robot.verificaEstado(self)
                    Robot.turn_right(self,speed_curva, 1)
                    print(esquerdo, " ", direito, " ", estado)

esquerdo = 0
direito = 0
estado = '0'
left = [0,0,0]
right = [0,0,0]
branco = [0,0,0,0,0,0]
preto = [0,0,0,0,0,0]
Corsa = Robot('outB','outD','in2','in4')
Corsa.abrirAprendizadoBranco()
Corsa.abrirAprendizadoPreto()
Corsa.follow_line(600,950)
#obs.: testar curva com duas rodas girando (uma muito pouco), com uma parada e outra girando ou com uma para cada lado

