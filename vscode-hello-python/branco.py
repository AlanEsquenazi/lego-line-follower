#!/usr/bin/env python3
# coding: utf-8

import ev3dev.ev3 as ev3
from ev3 import *
cor = ev3.ColorSensor('in1'); assert cor.connected
with open("branco.txt", "w") as branco:
    cor_lida = cor.raw()
    branco.write("%s", cor_lida);
