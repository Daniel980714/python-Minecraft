# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 10:59:29 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
import random
mc = Minecraft.create()
x,y,z = mc.player.getPos()
for i in range(500):
    r = random.randrange(1,5)
    if r==1:
        mc.setBlocks(x,y,z,x,y,z+5,1)
        z=z+5
    elif r==2:
        mc.setBlocks(x,y,z,x,y,z-5,1)
        z=z-5
    elif r==3:
        mc.setBlocks(x,y,z,x+5,y,z,1)
        x=x+5
    elif r==4:
        mc.setBlocks(x,y,z,x-5,y,z,1)
        x=x-5
    elif r==5:
        mc.setBlocks(x,y,z,x,y+5,z,1)
        y=y+5
    elif r==6:
        mc.setBlocks(x,y,z,x,y-5,z,1)
        y=y-5