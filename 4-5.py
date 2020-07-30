# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 14:19:47 2020

@author: appedu
"""
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
from random import randrange


for i in range(20):
    x,y,z = mc.player.getTilePos()
    x = x + i
    for j in range(20):
        color = randrange(0,16)
        z = z+1
        mc.setBlock(x,y,z,95,color)
        
t = 0
ans = randrange(0,16)
while True:
    hits = mc.events.pollBlockHits()
    if len(hits)>0:
        hit = hits[0]
        block = mc.getBlockWithData(hit.pos)
        data = block.data
        if data == ans:
            mc.postToChat('you win')
            mc.setBlock(hit.pos,57)
            break
        elif data<ans:
            mc.postToChat('Try bigger')
        elif data>ans:
            mc.postToChat('Try smaller')
        t = t + 1
        if t>5:
            mc.postToChat('oh')
            x,y,z = mc.player.getTilepos()
            mc.createExplosion(x,y,z)