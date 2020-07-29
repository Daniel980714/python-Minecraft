# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 15:07:52 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
x,y,z = mc.player.getTilePos()
for i in range(100):
    mc.setBlocks(x+i,y-i,z+i,x-i,y-i,z-i,24)
    time.sleep (0.5)