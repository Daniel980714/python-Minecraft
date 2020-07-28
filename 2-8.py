# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 14:57:57 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()

try:
    a = int(input('方塊ID?'))
    mc.setBlock(x,y-1,z,a)
except:
    print('請輸入數字')
    
