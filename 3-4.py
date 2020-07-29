# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 10:52:38 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
import random,time
pos = mc.player.getPos()
while True:
    x = pos.x+random.uniform(-125,125)
    z = pos.z+random.uniform(-125,125)
    y = pos.y+1
    mc.spawnEntity(x,y,z,20)