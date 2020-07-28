# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
while True:
    x,y,z = mc.player.getTilePos()
    a=mc.getBlock(x,y,z)
    if a==9:
        mc.setBlocks(x-1,y-1,z-1,x+1,y-1,z+1,19)