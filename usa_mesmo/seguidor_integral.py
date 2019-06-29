#!/usr/bin/env python3
# coding: utf-8
import ev3dev.ev3 as ev3
from ev3dev.ev3 import *
from enum import Enum
#from multiprocessing import Process
from time import sleep
from time import time

class States(Enum):
    Esquerda = -1
    Reto = 0
    Direita = 1

class Robot:
    def __init__(self,out1,out2,in1,in2,in3):

        self.lm1 = ev3.LargeMotor(out1); assert self.lm1.connected
        self.lm2 = ev3.LargeMotor(out2); assert self.lm2.connected
        self.se = ev3.ColorSensor(in1); assert self.se.connected
        self.sm = ev3.ColorSensor(in2); assert self.sm.connected
        self.sd = ev3.ColorSensor(in3); assert self.sd.connected
        #self.su = ev3.UltrasonicSensor(in4); assert self.su.connected

    def stop(self,time):
        self.lm1.run_timed(speed_sp = 0, time_sp = time, stop_action = 'coast')
        self.lm2.run_timed(speed_sp = 0, time_sp = time, stop_action = 'coast')
        self.lm1.wait_while("running")
        self.lm2.wait_while("running")

    def goForward(self,speed):
        self.lm1.run_forever(speed_sp = -speed)
        self.lm2.run_forever(speed_sp = -speed)

    def goBack(self,speed):
        self.lm1.run_forever(speed_sp = speed)
        self.lm2.run_forever(speed_sp = speed)

    def turnLeft(self,v_curva):
        self.lm2.run_forever(speed_sp = -v_curva)
        self.lm1.run_forever(speed_sp = v_curva)

    def turnRight(self,v_curva):
        self.lm2.run_forever(speed_sp = v_curva)
        self.lm1.run_forever(speed_sp = -v_curva)


    def curva_esquerda(self,speed_reta,speed_curva):
        while(not(esquerdo == 0 and meio == 1 and direito == 0)):
            while(meio == 0):
                Robot.verificaIntensidade(self)
                Robot.turnLeft(self,speed_curva)
                if(esquerdo == 0 and meio == 1 and direito == 0):
                    break
            while(meio == 1):
                Robot.verificaIntensidade(self)
                Robot.goForward(self,speed_reta)
                if(esquerdo == 0 and meio == 1 and direito == 0):
                    break

    def curva_direita(self,speed_reta,speed_curva):
        while(not(esquerdo == 0 and meio == 1 and direito == 0)):
            while(meio == 0):
                Robot.verificaIntensidade(self)
                Robot.turnRight(self,speed_curva)
                if(esquerdo == 0 and meio == 1 and direito == 0):
                    break
            while(meio == 1):
                Robot.verificaIntensidade(self)
                Robot.goForward(self,speed_reta)
                if(esquerdo == 0 and meio == 1 and direito == 0):
                    break


    def verificaIntensidade(self):
        global esquerdo
        global meio
        global direito
        global target
        global trigger
        global turn
        global errorLeft
        global errorRight
        global errorTotal
        global kp
        global ki
        global kd
        global correction
        global integral
        global derivative
        global lastError
        left = self.se.reflected_light_intensity
        middle = self.sm.reflected_light_intensity
        right = self.sd.reflected_light_intensity

        errorLeft = left - target
        errorRight = right - target
        errorTotal = -errorLeft + errorRight
        integral += errorTotal
        derivative = errorTotal - lastError
        correction = errorTotal * kp + integral * ki + derivative * kd


        lastError = errorTotal
        #correciton = (error * kp) + (integral * ki) + (derivative * kd)
        #error = target - value
        #integral = integral + error
        #derivative = error - last_error

        if(left < trigger): #preto
            esquerdo = 1
        else: #branco
            esquerdo = 0

        if(middle < trigger): #preto
            meio = 1
        else: #branco
            meio = 0

        if(right < trigger): #preto
            direito = 1
        else: #branco
            direito = 0

        print(left, " ", middle, " ", right)


    def seguidor(self,initialSpeed,speed_reta,speed_curva):
        if(esquerdo == 1 and direito == 0):
            Robot.curva_esquerda(self,speed_reta,speed_curva)
        elif(esquerdo == 0 and direito == 1):
            Robot.curva_direita(self,speed_reta,speed_curva)
        elif(esquerdo == 1 and direito == 1):
            self.lm1.run_forever(speed_sp = 0)
            self.lm2.run_forever(speed_sp = 0)
        elif(esquerdo == 0 and direito == 0):
            self.lm1.run_forever(speed_sp = -(initialSpeed - correction))
            self.lm2.run_forever(speed_sp = -(initialSpeed + correction))

    def verificaEncruzilhada(self):
        if((esquerdo == 1 and meio == 1) or (meio == 1 and direito == 1) or (esquerdo == 1 and direito == 1)):
            return False

    def seguirLinha(self,speed_reta,speed_curva):
        global esquerdo
        global meio
        global direito
        while(True):
            if(Robot.verificaEncruzilhada(self) == True):
                Robot.stop(self,100)
            else:
                Robot.verificaIntensidade(self)
                Robot.seguidor(self,speed_reta,speed_reta,speed_curva)


turn = 0
esquerdo = 0
direito = 0
meio = 0
trigger = 10
kp = 10
ki = 0 #-0.05
kd = 0
target = 55
errorLeft = 0
errorRight = 0
errorTotal = 0
correction = 0
integral = 0
derivative = 0
lastError = 0


#with open('estados.txt', "w") as arquivo:
#    arquivo.write("BEGIN")

Corsa = Robot('outB','outD','in2','in3','in4')
Sound.speak('Hello, I am Corsa')
Corsa.seguirLinha(150,90)
