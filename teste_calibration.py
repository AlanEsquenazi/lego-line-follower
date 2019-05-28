#!/usr/bin/env python3
# coding: utf-8
import ev3dev.ev3 as ev3
from ev3dev.ev3 import *
from enum import Enum
#from multiprocessing import Process
from time import sleep
from time import time
se = ev3.ColorSensor('in4'); assert se.connected

class Robot:
    def __init__(self):
        self.speed = 0
        self.time = 0

    def abrirAprendizadoBranco(self):
        global branco
        with open('branco_direito.txt', "r") as ft:            # a lista de aprendizado serah "azul, verde, vermelho"
            branco = ft.read().split(',')              # aqui, criamos uma lista de strings, cada elemento eh a cor
            branco.pop()
            branco = [int(x) for x in branco]     # tornamos as strings em inteiros

    def abrirAprendizadoPreto(self):
        global preto
        with open('preto_direito.txt', "r") as ft:            # a lista de aprendizado serah "azul, verde, vermelho"
            preto = ft.read().split(',')              # aqui, criamos uma lista de strings, cada elemento eh a cor
            preto.pop()
            preto = [int(x) for x in preto]     # tornamos as strings em inteiros

    def verificaCor(self):
        #TODO ver se mudando self. por Robot. e ver se funciona
        esq = se.raw
        if branco[0] - 30<=esq[0] and branco[1] + 30>=esq[0] and branco[2] - 30<=esq[1] and branco[3] + 30>=esq[1] and branco[4] - 30<=esq[2] and branco[5] + 30>=esq[2]:
            print(esq, " ", "BRANCO")
        elif preto[0] - 30<=esq[0] and preto[1] + 30>=esq[0] and preto[2] - 30<=esq[1] and preto[3] + 30>=esq[1] and preto[4] - 30<=esq[2] and preto[5] + 30>=esq[2]:
            print(esq, " ", "PRETO")

branco = [0,0,0,0,0,0]
preto = [0,0,0,0,0,0]
Teste = Robot()
Teste.abrirAprendizadoBranco()
Teste.abrirAprendizadoPreto()
print("branco", " ", branco, " ", "preto", " ", preto)
sleep(3)
while(True):
    Teste.verificaCor()
