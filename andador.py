#!/usr/bin/env python3
# coding: utf-8
import ev3dev.ev3 as ev3
from ev3dev.ev3 import *
from enum import Enum
#from multiprocessing import Process
from time import sleep
from time import time

class States(Enum):
    '''P = preto
    N = not(preto)'''
    NPP = 1
    PPN = 2
    NPN = 3
    PPP = 4
    NNP = 5
    PNN = 6
    NNN = 7
    PNP = 8

class Robot:
    def __init__(self,out1,out2,in1,in2,in3):

        self.lm1 = ev3.LargeMotor(out1); assert self.lm1.connected
        self.lm2 = ev3.LargeMotor(out2); assert self.lm2.connected
        self.se = ev3.ColorSensor(in1); assert self.se.connected
        self.sm = ev3.ColorSensor(in2); assert self.sm.connected
        self.sd = ev3.ColorSensor(in3); assert self.sd.connected

    def turn_left(self,speed,time):
        self.lm1.run_timed(speed_sp = 0, time_sp = 80, stop_action = 'coast')
        self.lm2.run_timed(speed_sp = -600, time_sp = 80, stop_action = 'coast')

    def turn_right(self,speed,time):
        self.lm1.run_timed(speed_sp = -600, time_sp = 80, stop_action = 'coast')
        self.lm2.run_timed(speed_sp = 0, time_sp = 80, stop_action = 'coast')

    def go_forward(self,speed,time):
        self.lm1.run_timed(speed_sp = -speed, time_sp = time, stop_action = 'coast')
        self.lm2.run_timed(speed_sp = -speed, time_sp = time, stop_action = 'coast')

    def stop(self,time):
        self.lm1.run_timed(speed_sp = 0, time_sp = time, stop_action = 'coast')
        self.lm2.run_timed(speed_sp = 0, time_sp = time, stop_action = 'coast')

    def curva_esquerda(self,speed,estado):
        self.lm1.run_timed(speed_sp = 0, time_sp = 500, stop_action = 'coast')
        self.lm2.run_timed(speed_sp = 0, time_sp = 500, stop_action = 'coast')
        while(not(meio == 1)):
            Robot.verificaCor(self)
            Robot.verificaEstado(self)
            Robot.verificaVerde(self)
            Robot.turn_left(self,speed, 60)
            Robot.stop(self,30)
            print(esquerdo, " ", meio, " ", direito, " ", estado)

    def curva_direita(self,speed,estado):
        self.lm1.run_timed(speed_sp = 0, time_sp = 500, stop_action = 'coast')
        self.lm2.run_timed(speed_sp = 0, time_sp = 500, stop_action = 'coast')
        while(not(meio == 1)):
            Robot.verificaCor(self)
            Robot.verificaEstado(self)
            Robot.verificaVerde(self)
            Robot.turn_right(self,speed, 60)
            Robot.stop(self,30)
            print(esquerdo, " ", meio, " ", direito, " ", estado)

    '''def meia_volta(self,speed, lendo_preto = 0, conta=0):
        global direito
        if not conta==2:
            Robot.curva_direita(self, speed, 50)
            Robot.verificaCor(self)
            if meio==1:
                    meia_volta(self, speed, 1,conta)
            if meio==0 and lendo_preto==1:
                    meia_volta(self,speed,0, 1)
            if meio==1 and conta==1:
                meia_volta(self,speed,1,2)'''


    def abrirAprendizadoBranco(self):
        global branco
        with open('branco.txt', "r") as ft:            # a lista de aprendizado serah "azul, verde, vermelho"
            branco = ft.read().split(',')              # aqui, criamos uma lista de strings, cada elemento eh a cor
            branco.pop()
            branco = [int(x) for x in branco]     # tornamos as strings em inteiros

    def abrirAprendizadoBranco_meio(self):
        global branco_meio
        with open('branco_meio.txt', "r") as ft:            # a lista de aprendizado serah "azul, verde, vermelho"
            branco_meio = ft.read().split(',')              # aqui, criamos uma lista de strings, cada elemento eh a cor
            branco_meio.pop()
            branco_meio = [int(x) for x in branco_meio]     # tornamos as strings em inteiros

    def abrirAprendizadoPreto(self):
        global preto
        with open('preto.txt', "r") as ft:            # a lista de aprendizado serah "azul, verde, vermelho"
            preto = ft.read().split(',')              # aqui, criamos uma lista de strings, cada elemento eh a cor
            preto.pop()
            preto = [int(x) for x in preto]     # tornamos as strings em inteiros

    def abrirAprendizadoPreto_meio(self):
        global preto_meio
        with open('preto_meio.txt', "r") as ft:            # a lista de aprendizado serah "azul, verde, vermelho"
            preto_meio = ft.read().split(',')              # aqui, criamos uma lista de strings, cada elemento eh a cor
            preto_meio.pop()
            preto_meio = [int(x) for x in preto_meio]     # tornamos as strings em inteiros

    def abrirAprendizadoVerde(self):
        global verde
        with open('verde.txt', "r") as ft:            # a lista de aprendizado serah "azul, verde, vermelho"
            verde = ft.read().split(',')              # aqui, criamos uma lista de strings, cada elemento eh a cor
            verde.pop()
            verde = [int(x) for x in verde]     # tornamos as strings em inteiros

    def verificaVerde(self):
        global e_verde
        global d_verde
        global verde

        if verde[0]<=left[0] and verde[1]>=left[0] and verde[2]<=left[1] and verde[3]>=left[1] and verde[4]<=left[2] and verde[5]>=left[2]:
            e_verde= True
        elif esquerdo == 0:
            e_verde = False
        if verde[0]<=right[0] and verde[1]>=right[0] and verde[2]<=right[1] and verde[3]>=right[1] and verde[4]<=right[2] and verde[5]>=right[2]:
            d_verde = True
        elif direito == 0:
            d_verde = False

    def verificaCor(self):
        # 1 preto e 0 branco
        global branco
        global branco_meio
        global preto
        global preto_meio
        global left
        global right
        global middle
        global esquerdo
        global direito
        global meio
        left = self.se.raw
        right = self.sd.raw
        middle = self.sm.raw
        if preto_meio[0]<=middle[0] and preto_meio[1]>=middle[0] and preto_meio[2]<=middle[1] and preto_meio[3]>=middle[1] and preto_meio[4]<=middle[2] and preto_meio[5]>=middle[2]:
            meio = 1
        else:
            meio = 0

        if preto[0]<=left[0] and preto[1]>=left[0] and preto[2]<=left[1] and preto[3]>=left[1] and preto[4]<=left[2] and preto[5]>=left[2]:
            esquerdo = 1
        else:
            esquerdo = 0

        if preto[0]<=right[0] and preto[1]>=right[0] and preto[2]<=right[1] and preto[3]>=right[1] and preto[4]<=right[2] and preto[5]>=right[2]:
            direito = 1
        else:
            direito = 0

    def verificaEstado(self):
        global esquerdo
        global direito
        global meio
        global estado
        if(esquerdo != 1 and meio == 1 and direito == 1): #NPP
            estado = States(1)
        if(esquerdo == 1 and meio == 1 and direito != 1): #PPN
            estado = States(2)
        if(esquerdo != 1 and meio == 1 and direito != 1): #NPN
            estado = States(3)
        if(esquerdo == 1 and meio == 1 and direito == 1): #PPP
            estado = States(4)
        if(esquerdo != 1 and meio != 1 and direito == 1): #NNP
            estado = States(5)
        if(esquerdo == 1 and meio != 1 and direito != 1): #PNN
            estado = States(6)
        if(esquerdo != 1 and meio != 1 and direito != 1): #NNN
            estado = States(7)
        if(esquerdo == 1 and meio != 1 and direito == 1): #PNP
            estado = States(8)


    def follow_line(self,speed_reta,speed_curva):
        while(True):
            global left
            global right
            global esquerdo
            global meio
            global direito
            global estado
            global e_verde
            global d_verde

            Robot.verificaCor(self)
            Robot.verificaEstado(self)
            Robot.verificaVerde(self)
            print(esquerdo, " ", meio, " ", direito, " ", estado)

            if(estado == States(1)): #caso NPP
                if(d_verde == True):
                    #curva para a direita
                    Robot.curva_direita(self,speed_curva,estado)
                else:
                    #segue reto
                    Robot.go_forward(self,speed_reta,30)

            if(estado == States(2)): #caso PPN
                if(e_verde == True):
                    #curva para a esquerda
                    Robot.curva_esquerda(self,speed_curva,estado)

                else:
                    #segue reto
                    Robot.go_forward(self,speed_reta,30)

            if(estado == States(3)): #caso NPN
                #segue reto
                Robot.go_forward(self,speed_reta,30)

            if(estado == States(4)): #caso PPP
                if(e_verde == True and d_verde == False):
                    #curva para a esquerda
                    Robot.curva_esquerda(self,speed_curva,estado)

                elif(e_verde == False and d_verde == True):
                    #curva para a direita
                    Robot.curva_direita(self,speed_curva,estado)

                '''elif(e_verde == True and d_verde == True):
                    #Robot.meia_volta(self,600)

                #elif(e_verde == False and d_verde == False):
                    #procurar verde
                    '''

            if(estado == States(5)): #caso NNP
                #curva para a direita
                Robot.curva_direita(self,speed_curva,estado)

            if(estado == States(6)): #caso PNN
                #curva para a esquerda
                Robot.curva_esquerda(self,speed_curva,estado)

            if(estado == States(7)): #caso NNN
                #segue reto
                Robot.go_forward(self,speed_reta,30)

            if(estado == States(8)): #caso PNP
                if(e_verde == True and d_verde == False):
                    #curva para a esquerda
                    Robot.curva_esquerda(self,speed_curva,estado)

                elif(e_verde == False and d_verde == True):
                    #curva para a direita
                    Robot.curva_direita(self,speed_curva,estado)

                elif(e_verde == True and d_verde == True):
                    meia_volta(self, 600)

                #elif(e_verde == False and d_verde == False):
                    #procurar verde

e_verde = False
d_verde = False
esquerdo = 0
direito = 0
meio = 0
estado = '0'
left = [0,0,0]
right = [0,0,0]
middle = [0,0,0]
branco = [0,0,0,0,0,0]
branco_meio = [0,0,0,0,0,0]
preto = [0,0,0,0,0,0]
preto_meio = [0,0,0,0,0,0]
verde = [0,0,0,0,0,0]
Corsa = Robot('outB','outD','in2','in3','in4')
Corsa.abrirAprendizadoBranco()
Corsa.abrirAprendizadoPreto()
Corsa.abrirAprendizadoBranco_meio()
Corsa.abrirAprendizadoPreto_meio()
Corsa.follow_line(600,950)


