#!/usr/bin/env python3
# coding: utf-8
import ev3dev.ev3 as ev3
from ev3dev.ev3 import *
from enum import Enum
#from multiprocessing import Process
from time import sleep
from time import time
se = ev3.ColorSensor('in2'); assert se.connected

class Robot:
    def __init__(self):
        self.speed = 0
        self.time = 0
        self.branco = [0,0,0,0,0,0]
        self.preto = [0,0,0,0,0,0]

    def abrirAprendizado(self,txt,color):
        with open(txt, "r") as ft:            # a lista de aprendizado serah "azul, verde, vermelho"
            color = ft.read().split(',')              # aqui, criamos uma lista de strings, cada elemento eh a cor
            color.pop()
            for i in range (len(color)):
                print("color[i]",color[i], '\n')
            for i in range(len(color)):
                color[i] = int(color[i])
              # tornamos as strings em inteiros

    def verificaCor(self):
        #TODO ver se mudando self. por Robot. e ver se funciona
        esq = se.raw
        #print(esq, " ", branco, " ", preto)
        #print(esq, '\n', self.branco)
        if self.branco[0] - 30<=esq[0] and self.branco[1] + 30>=esq[0] and self.branco[2] - 30<=esq[1] and self.branco[3] + 30>=esq[1] and self.branco[4] - 30<=esq[2] and self.branco[5] + 30>=esq[2]:
            #print("BRANCO/WHITE/BLANC")
            pass
        elif self.preto[0] - 30<=esq[0] and self.preto[1] + 30>=esq[0] and self.preto[2] - 30<=esq[1] and self.preto[3] + 30>=esq[1] and self.preto[4] - 30<=esq[2] and self.preto[5] + 30>=esq[2]:
            #print("PRETO/BLACK/NOIR")
            pass
Teste = Robot()
Teste.abrirAprendizado('branco.txt',Teste.branco)
Teste.abrirAprendizado('preto.txt',Teste.preto)
print("Teste.branco", Teste.branco)
while(True):
    Teste.verificaCor()



