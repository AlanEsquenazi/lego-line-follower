#!/usr/bin/env python3
# coding: utf-8

import ev3dev.ev3 as ev3
from ev3dev.ev3 import *
#from multiprocessing import Process
from time import sleep
from time import time

se = ev3.ColorSensor('in4'); assert se.connected

while(True):
    esq = se.value()
    if(esq == 1):
        print("Black")
    if(esq == 6):
        print("White")
