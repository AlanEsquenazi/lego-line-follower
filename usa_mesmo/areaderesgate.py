#!/usr/bin/env python3
# coding: utf-8
import ev3dev.ev3 as ev3
from ev3dev.ev3 import *
from enum import Enum
#from multiprocessing import Process
from time import sleep
from time import time
pesq = 800
pdir = 800
vel_curva = 60
comprimento = 0
largura = 0
uma_area = 2000
uma_unidade = 50
onde_ta = 0
class Robot:
    #def __init__(self,out1,out2,in1,in2,in3, in4):
    def __init__(self,out1,out2,in1,in2,in3, in4):

        self.lm1 = ev3.LargeMotor(out1); assert self.lm1.connected
        self.lm2 = ev3.LargeMotor(out2); assert self.lm2.connected
        self.se = ev3.ColorSensor(in1); assert self.se.connected
        self.sm = ev3.ColorSensor(in2); assert self.sm.connected
        self.sd = ev3.ColorSensor(in3); assert self.sd.connected
        self.us = ev3.UltrasonicSensor(in4); assert self.us.connected
    def go_forward(self,speed, time):
        self.lm1.run_timed(speed_sp = speed, time_sp = time, stop_action = 'coast')
        self.lm2.run_timed(speed_sp = speed, time_sp = time, stop_action = 'coast')

    def stop(self,time):
        self.lm1.run_timed(speed_sp = 0, time_sp = time, stop_action = 'coast')
        self.lm2.run_timed(speed_sp = 0, time_sp = time, stop_action = 'coast')

    def curva_esquerda(self,v_curva,pos_esq):
        self.lm1.run_to_rel_pos(position_sp = pos_esq, speed_sp = v_curva)
        self.lm2.run_to_rel_pos(position_sp =  -pos_esq, speed_sp = v_curva)
        self.lm1.wait_while("running")
        self.lm2.wait_while("running")

    def curva_direita(self,v_curva, pos_dir):
        self.lm1.run_to_rel_pos(position_sp = -pos_dir, speed_sp = v_curva)
        self.lm2.run_to_rel_pos(position_sp = pos_dir, speed_sp = v_curva)
        self.lm2.wait_while("running")
        self.lm1.wait_while("running")
    def mov1(self):
        global comprimento
        global largura
        global uma_unidade
        self.us.mode = 'US-DIST-CM'
        while(self.us.value()>50):
            Robot.go_forward(self, 100, uma_unidade)
            comprimento += 1
    def mov2(self):
        global comprimento
        global largura
        global uma_area
        global uma_unidade
        Robot.curva_esquerda(self, 60, pesq)
        Robot.go_forward(self, 100, uma_area)
        largura += uma_area/uma_unidade
        Robot.curva_direita(self, 60, pdir)
    def mov3(self, quem):
        global comprimento
        global largura
        global uma_unidade
        deu = 0
        while(self.us.value()>50):
            Robot.go_forward(self, 100, uma_unidade)
            deu +=1
        if(deu<5):
            onde_ta = quem
    def mov4(self):
        global comprimento
        global largura
        global uma_unidade
        self.us.mode = 'US-DIST-CM'
        while(self.us.value()>50):
            Robot.go_forward(self, 100, uma_unidade)
            largura += 1
    def mov5(self):
        global comprimento
        global largura
        global uma_area
        global uma_unidade
        Robot.curva_esquerda(self, 60, pesq)
        Robot.go_forward(self, 100, uma_area)
        comprimento += uma_area/uma_unidade
        Robot.curva_direita(self, 60, pdir)

    


Corsa = Robot('outB','outD','in2','in3','in4', 'in1')
Sound.speak('Hello, I am Corsa').wait()
Sound.speak('ATTENTION ATTENTION').wait()
Corsa.follow_line(100,100)
Corsa.mov1()
Corsa.mov2()
Corsa.mov3(1)
if(onde_ta==0):
    Corsa.mov4()
    Corsa.mov5()
    Corsa.mov3(2)
if(onde_ta==0):
    onde_ta = 3



