# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 16:18:12 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()

a = input('告示牌文字?')
mc.setSign(x,y,z,63,2,a)