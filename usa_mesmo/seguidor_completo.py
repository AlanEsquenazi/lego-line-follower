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
    PID = 2
    Encruzilhada = 3
    MeiaVolta = 4
    Obstaculo = 5

class Robot:
    def __init__(self,out1,out2,in1,in2,in3):

        self.lm1 = ev3.LargeMotor(out1); assert self.lm1.connected
        self.lm2 = ev3.LargeMotor(out2); assert self.lm2.connected
        self.se = ev3.ColorSensor(in1); assert self.se.connected
        self.sm = ev3.ColorSensor(in2); assert self.sm.connected
        self.sd = ev3.ColorSensor(in3); assert self.sd.connected
        #self.su = ev3.UltrasonicSensor(in4); assert self.su.connected

    def go_forward(self,speed):
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

    def corrigeReto(self,speed,time):
        self.lm1.run_timed(speed_sp = -speed, time_sp = time)
        self.lm2.run_timed(speed_sp = -speed,time_sp = time)
        self.lm1.wait_while("running")
        self.lm2.wait_while("running")

    def corrigeTras(self,speed,time):
        self.lm1.run_timed(speed_sp = speed, time_sp = time)
        self.lm2.run_timed(speed_sp = speed,time_sp = time)
        self.lm1.wait_while("running")
        self.lm2.wait_while("running")

    def corrigeDireita(self,speed,time):
        self.lm2.run_timed(speed_sp = -v_curva,time_sp = time)
        self.lm1.run_timed(speed_sp = v_curva,time_sp = time)
        self.lm1.wait_while("running")
        self.lm2.wait_while("running")

    def corrigeEsquerda(self,speed,time):
        self.lm2.run_timed(speed_sp = v_curva,time_sp = time)
        self.lm1.run_timed(speed_sp = -v_curva,time_sp = time)
        self.lm1.wait_while("running")
        self.lm2.wait_while("running")

    def stop(self,time):
        self.lm1.run_timed(speed_sp = 0, time_sp = time, stop_action = 'coast')
        self.lm2.run_timed(speed_sp = 0, time_sp = time, stop_action = 'coast')
        self.lm1.wait_while("running")
        self.lm2.wait_while("running")

    def go_forward_obstaculo(self,speed,pos):
        self.lm1.run_to_rel_pos(speed_sp = speed, position_sp = -pos)
        self.lm2.run_to_rel_pos(speed_sp = speed, position_sp = -pos)
        self.lm1.wait_while("running")
        self.lm2.wait_while("running")

    def curva_esquerda_obstaculo(self,v_curva,pos_esq):
        self.lm1.run_to_rel_pos(position_sp = pos_esq, speed_sp = v_curva)
        self.lm2.run_to_rel_pos(position_sp =  -pos_esq, speed_sp = v_curva)
        self.lm1.wait_while("running")
        self.lm2.wait_while("running")

    def curva_direita_obstaculo(self,v_curva, pos_dir):
        self.lm1.run_to_rel_pos(position_sp = -pos_dir, speed_sp = v_curva)
        self.lm2.run_to_rel_pos(position_sp = pos_dir, speed_sp = v_curva)
        self.lm2.wait_while("running")
        self.lm1.wait_while("running")

    def verificaCor(self):
        # 1 preto e 0 branco
        global branco
        global branco_meio
        global branco_direito
        global preto
        global preto_meio
        global preto_direito
        global left
        global right
        global middle
        global esquerdo
        global direito
        global meio
        global verde
        global verde_direito
        global direitoant
        global esquerdoant
        global e
        global m
        global d
        left = self.se.raw
        right = self.sd.raw
        middle = self.sm.raw
        esquerdoant = e
        direitoant = d
        if preto_meio[0]-10<=middle[0] and preto_meio[1]+10>=middle[0] and preto_meio[2]-10<=middle[1] and preto_meio[3]+10>=middle[1] and preto_meio[4]-10<=middle[2] and preto_meio[5]+10>=middle[2]:
            meio = 1

        elif branco_meio[0]-10<=middle[0] and branco_meio[1]+10>=middle[0] and branco_meio[2]-10<=middle[1] and branco_meio[3]+10>=middle[1] and branco_meio[4]-10<=middle[2] and branco_meio[5]+10>=middle[2]:
            meio = 0

        if preto[0]-10<=left[0] and preto[1]+10>=left[0] and preto[2]-10<=left[1] and preto[3]+10>=left[1] and preto[4]-10<=left[2] and preto[5]+10>=left[2]:
            e = 1

        elif verde[0] - 5<=left[0] and verde[1] + 5>=left[0] and verde[2] - 5<=left[1] and verde[3] + 5>=left[1] and verde[4] - 5<=left[2] and verde[5] + 5>=left[2]:
            e = 2

        elif branco[0]-10<=left[0] and branco[1]+10>=left[0] and branco[2]-10<=left[1] and branco[3]+10>=left[1] and branco[4]-10<=left[2] and branco[5]+10>=left[2]:
            e = 0

        if preto_direito[0]-10<=right[0] and preto_direito[1]+10>=right[0] and preto_direito[2]-10<=right[1] and preto_direito[3]+10>=right[1] and preto_direito[4]-10<=right[2] and preto_direito[5]+10>=right[2]:
            d = 1

        elif verde_direito[0] - 5<=right[0] and verde_direito[1] + 5>=right[0] and verde_direito[2] - 5<=right[1] and verde_direito[3] + 5>=right[1] and verde_direito[4] - 5<=right[2] and verde_direito[5] + 5>=right[2]:
            d = 2

        elif branco_direito[0]-10<=right[0] and branco_direito[1]+10>=right[0] and branco_direito[2]-10<=right[1] and branco_direito[3]+10>=right[1] and branco_direito[4]-10<=right[2] and branco_direito[5]+10>=right[2]:
            d = 0

        #if d == direitoant:  #fazer duas verificações para ter mais precisão
        direito = d
        #if e == esquerdoant:
        esquerdo = e

    def verificaIntensidade(self):
        global esquerdo
        global meio
        global direito
        global left
        global middle
        global right
        global trigger

        left = self.se.reflected_light_intensity
        middle = self.sm.reflected_light_intensity
        right = self.sd.reflected_light_intensity

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


    def PID(self):
        global target
        global trigger
        global turn
        global errorLeft
        global errorRight
        global kp
        global correctionLeft
        global correctionRight
        global integralLeft
        global integralRight
        global derivativeLeft
        global derivativeRight
        global lastErrorLeft
        global lastErrorRight
        global ki
        global kd

        errorLeft = left - target
        errorRight = right - target
        integralLeft += errorLeft
        integralRight += errorRight
        derivativeLeft = errorLeft - lastErrorLeft
        derivativeRight = errorRight - lastErrorRight
        correctionLeft = errorLeft * kp + integralLeft * ki + derivativeLeft * kd
        correctionRight = errorRight * kp + integralRight * ki + derivativeRight * kd

        lastErrorLeft = errorLeft
        lastErrorRight = errorRight
        #correciton = (error * kp) + (integral * ki) + (derivative * kd)
        #error = target - value
        #integral = integral + error
        #derivative = error - last_error

    def verificaEncruzilhada(self):
        if(esquerdo == 1 and meio == 1 and direito == 0):
            return True
        elif(esquerdo == 1 and meio == 0 and direito == 1):
            return True
        elif(esquerdo == 0 and meio == 1 and direito == 1):
            return True
        elif(esquerdo == 1 and meio == 1 and direito == 1):
            return True
        else:
            return False

    def verificaEstado(self):
        if(estado == States(-1)): #ESQUERDA
            if(esquerdo == 0 and meio == 1 and direito == 0):
                estado = States(2) #PID

        elif(estado == States(0)): #RETO
            if(esquerdo == 0 and meio == 1 and direito == 0):
                estado = States(2) #PID

        elif(estado == States(1)): #DIREITA
            if(esquerdo == 0 and meio == 1 and direito == 0):
                estado = States(2) #PID

        elif(estado == States(2)): #PID
            if(verificaEncruzilhada(self) == True):
                estado = States(3)
            #transição p obstaculo

        elif(estado == States(3)): #ENCRUZILHADA

        elif(estado == States(4)):
            if(esquerdo == 0 and meio == 1 and direito == 0):
                estado = States(2) #PID
        elif(estado == States(5)):
            #transição para pid

    def meiaVolta(self, sp_curv):
        Robot.stop(self,100)
        if(meio == 1):
            while(meio == 1):
                Robot.direita1(self,sp_curv)
            while(meio == 0):
                Robot.direita(self,sp_curv)
            while(meio == 1):
                Robot.direita1(self,sp_curv)
            while(meio == 0):
                Robot.direita(self,sp_curv)
        elif(meio == 0):
            while(meio == 0):
                Robot.direita(self,sp_curv)
            while(meio == 1):
                Robot.direita1(self,sp_curv)
            while(meio == 0):
                Robot.direita(self,sp_curv)
        estado = States(0)

    def encruzilhada(self):
        Robot.reposicionar(self)
        global estado
        global esquerdo
        global direito
        global viraEsquerda
        global viraDireita
        global jaReleu
        jaReleu = True
        viraEsquerda = False
        viraDireita = False
        Robot.reposicionar(self)
        while(not(esquerdo == 1 or direito == 1)):
            Robot.verificaCor(self)
            Robot.go_forward(self,40) #CALIBRAR
            if(esquerdo == 1):
                Robot.esquerda(self,90)
            elif(direito == 1):
                Robot.direita(self,90)

            if(esquerdo == 2):
                viraEsquerda = True
            if(direito == 2):
                viraDireita = True
        Robot.stop(self,100)
        if(viraEsquerda == True and viraDireita == False):
            Robot.corrige_reto(self,100,1000) #CALIBRAR
            estado = States(-1) #esquerda
        elif(viraEsquerda == False and viraDireita == True):
            Robot.corrige_reto(self,100,1000) #CALIBRAR
            estado = States(1) #direita
        elif(viraEsquerda == True and viraDireita == True):
            Robot.corrige_reto(self,100,1000) #CALIBRAR
            estado = States(4) #meia volta
        elif(viraEsquerda == False and viraDireita == False):
            Robot.corrige_reto(self,100,1000) #CALIBRAR
            estado = States(0) #reto

    def verificaDistancia(self,distancia_limite):
        global estado
        self.su.mode = 'US-DIST-CM'
        if(self.su.value() <= distancia_limite):
            estado = States(5)
            Robot.desviaObstaculo(self,150,60,950,800,800)

    def desviaObstaculo(self,speed_reta_obstaculo,speed_curva_obstaculo,posret,posesq,posdir):
        global estado
        if(estado == States(5)):
            Robot.curva_direita_obstaculo(self,speed_curva_obstaculo,0.50*posdir)
            Robot.go_forward_obstaculo(self,speed_reta_obstaculo,0.55*posret)
            Robot.curva_esquerda_obstaculo(self,speed_curva_obstaculo,0.47*posesq)
            Robot.go_forward_obstaculo(self,speed_reta_obstaculo,0.45*posret)
            Robot.curva_esquerda_obstaculo(self,speed_curva_obstaculo,0.5*posesq)
            Robot.go_forward_obstaculo(self,speed_reta_obstaculo,0.75*posret)
            Robot.curva_direita_obstaculo(self,speed_curva_obstaculo,0.5*posdir)
            Robot.go_forward_obstaculo(self,speed_reta_obstaculo,-0.15*posret) #vai pra trás
            if(meio == 0): #voltar a seguir linha
                if(esquerdo == 1):
                    estado = States(-1)
                elif(direito == 1):
                    estado = States(1)
                else:
                    estado = States(0)
            elif(meio == 1):
                estado = States(0)


    def reposicionar(self): #CALIBRAR
        Robot.stop(self,100)
        while(Robot.verificaEncruzilhada(self) == False): #enquanto não estiver em uma encruzilhada
            Robot.verificaIntensidade(self)
            if(esquerdo == 1):
                Robot.turnLeft(self,90)
            elif(direito == 1):
                Robot.turnRight(self,90)
            Robot.goBack(self,90)
        while(not(esquerdo == 0 and meio == 1 and direito == 0)): #enquanto não estiver corretamente posicionado
            Robot.verificaIntensidade(self)
            if(esquerdo == 1):
                Robot.turnLeft(self,90)
            elif(direito == 1):
                Robot.turnRight(self,90)
            Robot.goBack(self,90)
        Robot.corrigeTras(self,200,600)

    def seguidor(self,initialSpeed):
        self.lm1.run_forever(speed_sp = -(initialSpeed + correctionLeft))
        self.lm2.run_forever(speed_sp = -(initialSpeed + correctionRight))

    def seguirLinha(self,speed_reta,speed_curva):
        global esquerdo
        global meio
        global direito
        global estado
        while(True):
            Robot.verificaIntensidade(self)
            Robot.verificaEstado(self)
            if(estado == States(-1)): #ESQUERDA
                Robot.turnLeft(self,speed_curva)
            elif(estado == States(0)): #RETO
                Robot.go_forward(self,speed_reta)

            elif(estado == States(1)): #DIREITA
                Robot.verificaIntensidade(self)
                Robot.turnRight(self,speed_reta)

            elif(estado == States(2)): #PID
                Robot.verificaDistancia(self,135) #CALIBRAR
                Robot.PID(self)
                Robot.seguidor(self,150) #CALIBRAR

            elif(estado == States(3)): #ENCRUZILHADA
                Robot.encruzilhada(self)

            elif(estado == States(4)): #MEIA VOLTA
                Robot.MeiaVolta(self)

            #elif(estado == States(5)): #OBSTACUlO





turn = 0
esquerdo = 0
direito = 0
meio = 0
trigger = 28
kp = 10
ki = -0.01
kd = 1
target = 50
errorLeft = 0
errorRight = 0
correctionLeft = 0
correcitonRight = 0
integralLeft = 0
integralRight = 0
derivativeLeft = 0
derivativeRight = 0
lastErrorLeft = 0
lastErrorRight = 0

#with open('estados.txt', "w") as arquivo:
#    arquivo.write("BEGIN")

Corsa = Robot('outB','outD','in2','in3','in4')
Sound.speak('Hello, I am Corsa')
Corsa.seguirLinha(200,90)