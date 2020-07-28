# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 14:49:46 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()

x=1
y=1
z=1

time.sleep(5)

while y<100:
    mc.player.setTilePos(x,y,z)
    time.sleep(0.1)
    y=y+1