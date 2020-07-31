# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
x,y,z = mc.player.getTilePos()
for i in range(30):
    mc.setBlocks(x+i,y-i,z+i,x-i,y-i,z-i,24)
    time.sleep (0.2)