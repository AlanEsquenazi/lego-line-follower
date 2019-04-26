#!/usr/bin/env python3
# coding: utf-8
import ev3dev.ev3 as ev3
from ev3dev.ev3 import *
from enum import Enum
#from multiprocessing import Process
from time import sleep
from time import time

lm1 = ev3.LargeMotor('outB'); assert lm1.connected
lm2 = ev3.LargeMotor('outD'); assert lm2.connected

lm1.run_forever(speed_sp = 100,stop_action = 'coast')
lm2.run_forever(speed_sp = 800,stop_action = 'coast')
