#!/usr/bin/env python3
# coding: utf-8
import ev3dev.ev3 as ev3
from ev3dev.ev3 import *
from enum import Enum
#from multiprocessing import Process
from time import sleep
from time import time

class States(Enum):
    VerdeEsquerda = -2
    Esquerda = -1
    Reto = 0
    Direita = 1
    VerdeDireita = 2
    VerdeMeiaVolta = 3


class Robot:
    def __init__(self, in3):
        self.sd = ev3.ColorSensor(in3); assert self.sd.connected

    def abrirAprendizadoPreto(self):
        global preto
        with open('preto_meio.txt', "r") as ft:            # a lista de aprendizado serah "azul, verde, vermelho"
            preto = ft.read().split(',')              # aqui, criamos uma lista de strings, cada elemento eh a cor
            preto.pop()
            preto = [int(x) for x in preto]     # tornamos as strings em inteiros



    def verificaCor(self):
        # 1 preto e 0 branco
        global branco
        global preto
        global right
        global direito
        global verde
        right = self.sd.raw


        if preto[0] - 10<=right[0] and preto[1] + 10>=right[0] and preto[2] - 10<=right[1] and preto[3] + 10>=right[1] and preto[4] - 10<=right[2] and preto[5] + 10>=right[2]:
            direito = 1

        else:
            direito = 0

        print(right, " ", direito)
        with open("meio.txt", "a") as arquivo:
            arquivo.write(str(right))
            arquivo.write(" ")
            arquivo.write(str(direito))
            arquivo.write('\n')




direito = 0
right = [0,0,0]
branco = [0,0,0,0,0,0]
preto = [0,0,0,0,0,0]
Corsa = Robot('in3')
Sound.speak('Hello, I am Corsa').wait()

Corsa.abrirAprendizadoPreto()
while(1):
    Corsa.verificaCor()


