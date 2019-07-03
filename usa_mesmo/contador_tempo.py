#!/usr/bin/env python3
# coding: utf-8
import ev3dev.ev3 as ev3
from ev3dev.ev3 import *
from enum import Enum
#from multiprocessing import Process
from time import sleep
from time import time

while(True):
    tempo1 = time.time()
    Sound.speak("A").wait()
    tempo2 = tempo1
    print(tempo2 - tempo1)
