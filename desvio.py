#!/usr/bin/env python3
# coding: utf-8
import ev3dev.ev3 as ev3
from ev3dev.ev3 import *
from enum import Enum
#from multiprocessing import Process
from time import sleep
from time import time
posicaodir = 413           # as curvas
posicaoesq = 411
class Robot_US:
    def __init__(self,out1,out2,in1):

        self.lm1 = ev3.LargeMotor(out1); assert self.lm1.connected
        self.lm2 = ev3.LargeMotor(out2); assert self.lm2.connected
        self.us = ev3.UltrasonicSensor(in1); assert self.us.connected

    def stop(self,time):
        self.lm1.run_timed(speed_sp = 0, time_sp = time, stop_action = 'coast')
        self.lm2.run_timed(speed_sp = 0, time_sp = time, stop_action = 'coast')

    def turn_left(self,speed,time):
        self.lm1.run_timed(speed_sp = speed, time_sp = time, stop_action = 'coast')
        self.lm2.run_timed(speed_sp = 0, time_sp = time, stop_action = 'coast')

    def turn_right(self,speed,time):
        self.lm1.run_timed(speed_sp = 0, time_sp = time, stop_action = 'coast')
        self.lm2.run_timed(speed_sp = speed, time_sp = time, stop_action = 'coast')

    def go_forward(self,speed,time):
        self.lm1.run_timed(speed_sp = -speed, time_sp = time, stop_action = 'coast')
        self.lm2.run_timed(speed_sp = -speed, time_sp = time, stop_action = 'coast')
    def curva_esquerda(self,v_curva,pos_esq):
        print("curva esquerda")
        #Robot.verificaCor(self)
        #Robot.verificaEstado(self)
        #Robot.verificaVerde(self)
        #print(esquerdo, " ", meio, " ", direito, " ", estado)
        self.lm2.run_to_rel_pos(position_sp =  0, speed_sp = v_curva)
        self.lm1.run_to_rel_pos(position_sp = pos_esq, speed_sp = v_curva)
        self.lm2.wait_while("running")
        self.lm1.wait_while("running")

    def curva_direita(self,v_curva, pos_dir):
        print("curva direita")
        #Robot.verificaCor(self)
        #Robot.verificaEstado(self)
        #Robot.verificaVerde(self)
        print(esquerdo, " ", meio, " ", direito, " ", estado)
        self.lm2.run_to_rel_pos(position_sp =  pos_dir, speed_sp = v_curva)
        self.lm1.run_to_rel_pos(position_sp = 0, speed_sp = v_curva)
        self.lm2.wait_while("running")
        self.lm1.wait_while("running")

    def desvia_do_obstaculo(self, speed, time, p_dir,p_esq):
        Robot_US.curva_direita(self, speed, p_dir)
        Robot_US.go_forward(self,speed,time)
        Robot_US.curva_esquerda(self, speed, p_esq)
        Robot_US.go_forward(self,speed,time)
        Robot_US.curva_esquerda(self, speed, p_esq)
        Robot_US.go_forward(self,speed,time)
        Robot_US.curva_direita(self, speed, p_dir)

    def encontrar_obstaculo(self):
        global posicaodir
        global posicaoesq
        self.us.mode = 'US-DIST-CM'
        if(self.us.value()<=50):
            Robot_US.desvia_do_obstaculo(self, 600,950,posicaodir, posicaoesq)

corsinha2  = Robot_US("outB", "outD", "in4")
while(1):
    corsinha2.encontrar_obstaculo()




