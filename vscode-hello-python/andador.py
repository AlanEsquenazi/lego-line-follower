#!/usr/bin/env python3
# coding: utf-8

import ev3dev.ev3 as ev3
#from multiprocessing import Process
from time import sleep
from time import time
gyro = GyroSensor()

lm1 = ev3.LargeMotor('outA')
lm2 = ev3.LargeMotor('outB')
steer_pair = ev3.MoveSteering('outA', 'outB', motor_class=LargeMotor)

#anda pra frente
steer_pair.on_for_seconds(steering=0, speed=50, seconds=3)
sleep(1)

#anda pra direita x ângulos
a1 = gyro.angle()
a2 = 0
while(a2 < a1)
    steer_pair.on_for_seconds(steering=100, speed=50, seconds=1)
    sleep(1)
    a2 = gyro.angle()

#anda pra frente
steer_pair.on_for_seconds(steering=0, speed=50, seconds=3)
sleep(1)


