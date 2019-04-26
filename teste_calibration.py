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
        branco = [0,0,0,0,0,0]
        preto = [0,0,0,0,0,0]

    def abrirAprendizado(self,txt,color):
        with open('branco.txt', "r") as ft:            # a lista de aprendizado serah "azul, verde, vermelho"
            color = ft.read().split(',')              # aqui, criamos uma lista de strings, cada elemento eh a cor
            color.pop()
            for x in color:
                print("x", x, "int(x)", int(x))
            color = [int(x) for x in color]     # tornamos as strings em inteiros
        print(branco, " ", preto)

    def verificaCor(self):
        esq = se.raw
        #print(esq, " ", branco, " ", preto)
        if branco[0] - 30<=esq[0] and branco[1] + 30>=esq[0] and branco[2] - 30<=esq[1] and branco[3] + 30>=esq[1] and branco[4] - 30<=esq[2] and branco[5] + 30>=esq[2]:
            print("BRANCO/WHITE/BLANC")
        elif preto[0] - 30<=esq[0] and preto[1] + 30>=esq[0] and preto[2] - 30<=esq[1] and preto[3] + 30>=esq[1] and preto[4] - 30<=esq[2] and preto[5] + 30>=esq[2]:
            print("PRETO/BLACK/NOIR")
Teste = Robot()
Teste.abrirAprendizado('branco.txt',branco)
Teste.abrirAprendizado('preto.txt',preto)
while(True):
    Teste.verificaCor()



