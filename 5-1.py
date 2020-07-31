# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
for i in range(30):
    mc.setBlocks(x+i,y-i-1,z+i,x-i,y-i-1,z-i,24)
for j in range(28):
    mc.setBlocks(x+j,y-j-2,z+j,x-j,y-j-2,z-j,0)