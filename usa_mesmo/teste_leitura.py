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
    def __init__(in3):

        self.sd = ev3.ColorSensor(in3); assert self.sd.connected

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


    def abrirAprendizadoVerde(self):
        global verde
        with open('verde_direito.txt', "r") as ft:            # a lista de aprendizado serah "azul, verde, vermelho"
            verde = ft.read().split(',')              # aqui, criamos uma lista de strings, cada elemento eh a cor
            verde.pop()
            verde = [int(x) for x in verde]     # tornamos as strings em inteiros

    def verificaCor(self):
        # 1 preto e 0 branco
        global branco
        global preto
        global right
        global direito
        global verde
        right = self.sd.raw


        if preto_direito[0]<=right[0] and preto_direito[1]>=right[0] and preto_direito[2]<=right[1] and preto_direito[3]>=right[1] and preto_direito[4]<=right[2] and preto_direito[5]>=right[2]:
            direito = 1

        elif verde_direito[0] - 10<=left[0] and verde_direito[1] + 10>=left[0] and verde_direito[2] - 10<=left[1] and verde_direito[3] + 10>=left[1] and verde_direito[4] - 10<=left[2] and verde_direito[5] + 10>=left[2]:
            direito = 2

        else:
            direito = 0

        print(direito)




direito = 0
right = [0,0,0]
branco = [0,0,0,0,0,0]
preto = [0,0,0,0,0,0]
verde = [0,0,0,0,0,0]
Corsa = Robot('in4')
Sound.speak('Hello, I am Corsa').wait()

Corsa.abrirAprendizadoBranco()
Corsa.abrirAprendizadoPreto()
Corsa.abrirAprendizadoVerde()
Corsa.verificaCor()


