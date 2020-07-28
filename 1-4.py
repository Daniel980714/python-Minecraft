# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 15:29:42 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()

mc.postToChat("I'm watching you.")

while True:
    x,y,z = mc.player.getTilePos()
    mc.postToChat("You are located on X:"+str(x)
                                    +", Y:"+str(y)
                                    +", Z:"+str(z))