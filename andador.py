#!/usr/bin/env python3
# coding: utf-8
import ev3dev.ev3 as ev3
from ev3dev.ev3 import *
from enum import Enum
#from multiprocessing import Process
from time import sleep
from time import time

class States(Enum):
    #P = preto
    #N = not(preto)
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
        #conecta os sensores e motores
        self.lm1 = ev3.LargeMotor(out1); assert self.lm1.connected
        self.lm2 = ev3.LargeMotor(out2); assert self.lm2.connected
        self.se = ev3.ColorSensor(in1); assert self.se.connected
        self.sm = ev3.ColorSensor(in2); assert self.sm.connected
        self.sd = ev3.ColorSensor(in3); assert self.sd.connected

    def turn_left(self,speed,time):
        #função crua para virar para esquerda
        self.lm1.run_timed(speed_sp = speed, time_sp = time, stop_action = 'coast')
        self.lm2.run_timed(speed_sp = -speed, time_sp = time, stop_action = 'coast')

    def turn_right(self,speed,time):
        #função crua para virar para direita
        self.lm1.run_timed(speed_sp = -speed, time_sp = time, stop_action = 'coast')
        self.lm2.run_timed(speed_sp = speed, time_sp = time, stop_action = 'coast')

    def go_forward(self,speed,time):
        #função para seguir reto
        self.lm1.run_timed(speed_sp = -speed, time_sp = time, stop_action = 'coast')
        self.lm2.run_timed(speed_sp = -speed, time_sp = time, stop_action = 'coast')

    def curva_esquerda(self,speed,estado):
        #função para fazer curva enquanto segue linha
        self.lm1.run_timed(speed_sp = 0, time_sp = 500, stop_action = 'coast')
        self.lm2.run_timed(speed_sp = 0, time_sp = 500, stop_action = 'coast')
        while(not(estado == States(3))):
            Robot.verificaCor(self)
            Robot.verificaEstado(self)
            Robot.verificaVerde(self)
            Robot.turn_left(self,speed, 60)
            print(esquerdo, " ", direito, " ", estado)

    def curva_direita(self,speed,estado):
        #função para fazer curva enquanto segue linha
        self.lm1.run_timed(speed_sp = 0, time_sp = 500, stop_action = 'coast')
        self.lm2.run_timed(speed_sp = 0, time_sp = 500, stop_action = 'coast')
        while(not(estado == States(3))):
            Robot.verificaCor(self)
            Robot.verificaEstado(self)
            Robot.verificaVerde(self)
            Robot.turn_right(self,speed, 60)
            print(esquerdo, " ", direito, " ", estado)

    def abrirAprendizadoBranco(self):
        #converte o branco.txt em uma lista
        global branco
        with open('branco.txt', "r") as ft:            # a lista de aprendizado serah "azul, verde, vermelho"
            branco = ft.read().split(',')              # aqui, criamos uma lista de strings, cada elemento eh a cor
            branco.pop()
            branco = [int(x) for x in branco]     # tornamos as strings em inteiros

    def abrirAprendizadoPreto(self):
        #converte o preto.txt em uma lista
        global preto
        with open('preto.txt', "r") as ft:            # a lista de aprendizado serah "azul, verde, vermelho"
            preto = ft.read().split(',')              # aqui, criamos uma lista de strings, cada elemento eh a cor
            preto.pop()
            preto = [int(x) for x in preto]     # tornamos as strings em inteiros

    def abrirAprendizadoVerde(self):
        #converte o verde.txt em uma lista
        global verde
        with open('verde.txt', "r") as ft:            # a lista de aprendizado serah "azul, verde, vermelho"
            verde = ft.read().split(',')              # aqui, criamos uma lista de strings, cada elemento eh a cor
            verde.pop()
            verde = [int(x) for x in verde]     # tornamos as strings em inteiros

    def verificaVerde(self):
        #verifica se o verde foi lido
        global e_verde
        global d_verde
        global esquerdo
        global direito
        if(verde[0]<=left[0] and verde[1]>=left[0] and verde[2]<=left[1] and verde[3]>=left[1] and verde[4]<=left[2] and verde[5]>=left[2]):
            e_verde = True

        elif(esquerdo == False): #se lê branco do lado esquerdo
            e_verde = False

        if(verde[0]<=right[0] and verde[1]>=right[0] and verde[2]<=right[1] and verde[3]>=right[1] and verde[4]<=right[2] and verde[5]>=right[2]):
            d_verde = True

        elif(direito == False): #se lê branco do lado direito
            d_verde = False

        '''def meia_volta(self):
            #dá a meia volta quando lê dois verdes
            self.lm1.run_timed(speed_sp = 0, time_sp = 500, stop_action = 'coast')
            self.lm2.run_timed(speed_sp = 0, time_sp = 500, stop_action = 'coast')
            while():
                Robot.turn_right(self,speed, 60)'''




   ''' def verificaPreto(self):
        global d_preto
        if(direito == True):       #TODO PENSAR NESSA PORRA
            direito == True
        elif(direito == False):'''

    def verificaCor(self):
        # 1 preto e 0 branco
        global left
        global right
        global middle
        global esquerdo
        global direito
        global meio

        left = self.se.raw
        right = self.sd.raw
        middle = self.sm.raw

        if branco[0]<=middle[0] and branco[1]>=middle[0] and branco[2]<=middle[1] and branco[3]>=middle[1] and branco[4]<=middle[2] and branco[5]>=middle[2]:
            meio = 0
        elif preto[0]<=middle[0] and preto[1]>=middle[0] and preto[2]<=middle[1] and preto[3]>=middle[1] and preto[4]<=middle[2] and preto[5]>=middle[2]:
            meio = 1
        else:
            meio = -1
        if branco[0]<=left[0] and branco[1]>=left[0] and branco[2]<=left[1] and branco[3]>=left[1] and branco[4]<=left[2] and branco[5]>=left[2]:
            esquerdo = 0
        elif preto[0]<=left[0] and preto[1]>=left[0] and preto[2]<=left[1] and preto[3]>=left[1] and preto[4]<=left[2] and preto[5]>=left[2]:
            esquerdo = 1
        else:
            esquerdo = -1
        if branco[0]<=right[0] and branco[1]>=right[0] and branco[2]<=right[1] and branco[3]>=right[1] and branco[4]<=right[2] and branco[5]>=right[2]:
            direito = 0
        elif preto[0]<=right[0] and preto[1]>=right[0] and preto[2]<=right[1] and preto[3]>=right[1] and preto[4]<=right[2] and preto[5]>=right[2]:
            direito = 1
        else:
            direito = -1

    def verificaEstado(self):
        global esquerdo
        global direito
        global estado

        if esquerdo != 1 and meio == 1 and direito == 1: #NPP
            estado = States(1)
        if esquerdo == 1 and meio == 1 and direito != 1: #PPN
            estado = States(2)
        if esquerdo != 1 and meio == 1 and direito != 1: #NPN
            estado = States(3)
        if esquerdo == 1 and meio == 1 and direito == 1: #PPP
            estado = States(4)
        if esquerdo != 1 and meio != 1 and direito == 1: #NNP
            estado = States(5)
        if esquerdo == 1 and meio != 1 and direito != 1: #PNN
            estado = States(6)
        if esquerdo != 1 and meio != 1 and direito != 1: #NNN
            estado = States(7)
        if esquerdo == 1 and meio != 1 and direito == 1: #PNP
            estado = States(8)

    def follow_line(self,speed_reta,speed_curva):
        while(True):
            global e_verde
            global d_verde
            global left
            global right
            global esquerdo
            global direito
            global estado
            Robot.verificaVerde(self)
            Robot.verificaCor(self)
            Robot.verificaEstado(self)
            print(esquerdo, " ", direito, " ", estado)

            if(estado == States(1)): #NPP
                if(d_verde == True):
                    #curva direita
                    curva_direita(self,speed_curva,estado)
                else:
                    #segue reto
                    Robot.go_forward(self,speed_reta, 30)

            if(estado == States(2)): #PPN
                if(e_verde == True):
                    #curva esquerda
                    curva_esquerda(self,speed_curva,estado)
                else:
                    #segue reto
                    Robot.go_forward(self,speed_reta, 30)

            if(estado == States(3)): #NPN
                #segue reto
                Robot.go_forward(self,speed_reta, 30)

            if(estado == States(4)): #PPP
                if(e_verde == True and d_verde == False):
                    #curva esquerda
                    curva_esquerda(self,speed_curva,estado)
                if(e_verde == False and d_verde == True):
                    #curva direita
                    curva_direita(self,speed_curva,estado)
                if(e_verde == True and d_verde == True):
                    #meia volta
                if(e_verde == False and d_verde == False):
                    #procurar verde

            if(estado == States(5)): #NNP
                #curva direita
                curva_direita(self,speed_curva,estado)

            if(estado == States(6)): #PNN
                #curva esquerda
                curva_esquerda(self,speed_curva,estado)

            if(estado == States(7)): #NNN
                #segue reto
                Robot.go_forward(self,speed_reta, 30)

            if(estado == States(8)): #PNP
                if(e_verde == True and d_verde == False):
                    #curva esquerda
                    curva_esquerda(self,speed_curva,estado)
                if(e_verde == False and d_verde == True):
                    #curva direita
                    curva_direita(self,speed_curva,estado)
                if(e_verde == True and d_verde == True):
                    #meia volta
                if(e_verde == False and d_verde == False):
                    #procurar verde

esquerdo = 0
direito = 0
meio = 0
estado = '0'
left = [0,0,0]
right = [0,0,0]
middle = [0,0,0]
branco = [0,0,0,0,0,0]
preto = [0,0,0,0,0,0]
Corsa = Robot('outB','outD','in2','in3','in4')
Corsa.abrirAprendizadoBranco()
Corsa.abrirAprendizadoPreto()
Corsa.follow_line(600,950)
#obs.: testar curva com duas rodas girando (uma muito pouco), com uma parada e outra girando ou com uma para cada lado

