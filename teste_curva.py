#!/usr/bin/env python3
# coding: utf-8
import ev3dev.ev3 as ev3
from ev3dev.ev3 import *
from enum import Enum
#from multiprocessing import Process
from time import sleep
from time import time

motorEsq = ev3.LargeMotor('outB'); assert motorEsq.connected
motorDir = ev3.LargeMotor('outD'); assert motorDir.connected


def stop(time):
    lm1.run_timed(speed_sp = 0, time_sp = time, stop_action = 'coast')
    lm2.run_timed(speed_sp = 0, time_sp = time, stop_action = 'coast')

def curva_esquerda(v_curva,pos_esq):
        motorDir.run_to_rel_pos(position_sp = pos_esq, speed_sp = v_curva)
        motorEsq.run_to_rel_pos(position_sp = - pos_esq, speed_sp = v_curva)
        motorDir.wait_while("running")
        motorEsq.wait_while("running")


curva_esquerda(400,460)


