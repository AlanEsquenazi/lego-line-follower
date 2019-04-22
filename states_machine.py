#!/usr/bin/env python3
# coding: utf-8

import ev3dev.ev3 as ev3
from ev3dev.ev3 import *
#from multiprocessing import Process
from time import sleep
from time import time

lm1 = ev3.LargeMotor('outD'); assert lm1.connected
lm2 = ev3.LargeMotor('outA'); assert lm2.connected

se = ev3.ColorSensor('in2'); assert se.connected
sd = ev3.ColorSensor('in4'); assert sd.connected

class Robot:
    def __init__(self):
        self.speed = 0
        self.time = 0
    def turn_left(self,speed,time):
        lm1.run_timed(speed_sp = -speed, time_sp = time, stop_action = 'coast')
        lm2.run_timed(speed_sp = speed, time_sp = time, stop_action = 'coast')
    def turn_right(self,speed,time):
        lm1.run_timed(speed_sp = speed, time_sp = time, stop_action = 'coast')
        lm2.run_timed(speed_sp = -speed, time_sp = time, stop_action = 'coast')
    def go_forward(self,speed,time):
        lm1.run_timed(speed_sp = -1*speed, time_sp = time, stop_action = 'coast')
        lm2.run_timed(speed_sp = -1*speed, time_sp = time, stop_action = 'coast')


class Calibration(Robot):
    def __init__(self):
        Robot.__init__(self)

    def white():
        with open("white_esq.txt", "w") as white_esq:
            esq_lida = se.raw
            esq_lida = str(esq_lida)
            white_esq.write(esq_lida);


        with open("white_dir.txt", "w") as white_dir:
            dir_lida = sd.raw
            dir_lida = str(dir_lida)
            white_dir.write(dir_lida);

    def black():
        with open("black_esq.txt", "w") as black_esq:
            esq_lida = se.raw
            esq_lida = str(esq_lida)
            black_esq.write(esq_lida);

        with open("black_dir.txt", "w") as black_dir:
            dir_lida = sd.raw
            dir_lida = str(dir_lida)
            black_dir.write(dir_lida);

    '''def abrirAprendizado():
    ## try: tenta abrir um arquivo de aprendizado
    try:
        with open("aprendizado.txt", "r") as ft:            # a lista de aprendizado serah "azul, verde, vermelho"
            robot.aprendizado = ft.read().split(',')              # aqui, criamos uma lista de strings, cada elemento eh a cor
            robot.aprendizado.pop()
            for x in robot.aprendizado:
                print("x", x, "int(x)", int(x))
            robot.aprendizado = [int(x) for x in robot.aprendizado]     # tornamos as strings em inteiros
    except:
        robot.aprendizado = [47, 47, 47]                         # caso nao haja arquivo, criamos a lista
    return robot.aprendizado                                  # Retorna a lista "aprendizado"
'''
class LineFollower(Robot):
    def __init__(self):
        Robot.__init__(self)

    def follow(self):
        #obs.: sem calibração, primeiro vamos testar com a leitura padrão do sensor
        esq = se.value()
        dir = sd.value()
        print(esq, " ", dir, '\n')
        if(esq>25 and esq<40 and dir>25 and dir<40 ): #white and white
            Robot.go_forward(self, self.speed, 1)

        if(esq < 25 and dir < 25): #black and black
            sleep(1)
        else:
            if(esq<25 and dir>25 and dir<40 ): #black and white
                while(not(esq>25 and esq<40 and dir>25 and dir<40)):
                    Robot.turn_left(self, self.speed, 1)
                    print(esq, " ", dir, '\n')
                    print("esquerda")
            if(esq>25 and esq<40 and dir<25): #white and black
                while(not (esq>25 and esq<40 and dir>25 and dir<40)):
                    Robot.turn_right(self, self.speed, 1)
                    print("direita")
                    print(esq, " ", dir, '\n')

#APLICAR CALIBRAÇÃO
Corsa = LineFollower()
Corsa.speed = 400
Corsa.time = 1000
#Corsa.white()
#Corsa.black()
while(True):
    Corsa.follow()

