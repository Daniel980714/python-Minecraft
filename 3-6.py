# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 14:00:14 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
def tree(x,y,z):
    mc.setBlocks(x-2,y+3,z-2,x+2,y+3,z+2,57)
    mc.setBlocks(x-1,y+4,z-1,x+1,y+5,z+1,57)
    mc.setBlocks(x,y+6,z,x,y+7,z,57)
    mc.setBlocks(x,y,z,x,y+4,z,17)

for i in range(10):
    for j in range(10):
        for k in range(10):
            tree(x+k*5,y+i*j,z+j*10)
            