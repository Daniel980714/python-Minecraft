# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 10:10:25 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
n = 1
for i in range(10):
    for j in range(n):
        mc.spawnEntity(x,y,z,60)
    n = n*2