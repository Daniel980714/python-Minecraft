# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 14:19:30 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
a=0

while a<20:
    mc.setBlocks(x,y,z,x,y+9,z+60,19)
    x = x+3
    a=a+2