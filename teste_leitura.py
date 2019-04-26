#!/usr/bin/env python3
# coding: utf-8
import ev3dev.ev3 as ev3
from ev3dev.ev3 import *
from enum import Enum
#from multiprocessing import Process
from time import sleep
from time import time

with open('branco.txt', "r") as ft:            # a lista de aprendizado serah "azul, verde, vermelho"
            branco = ft.read().split(',')              # aqui, criamos uma lista de strings, cada elemento eh a cor
            branco.pop()
            for x in branco:
                print("x", x, "int(x)", int(x))
            branco = [int(x) for x in branco]     # tornamos as strings em inteiros

print(branco)

while(True):
    sleep(1)
