# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 11:44:30 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()

for i in range (20):
    mc.setBlock(x+i,y-1,z+i,1)
    mc.setBlock(x+i+1,y-1,z+i,1)
    mc.setBlock(x+i+2,y-1,z+i,1)