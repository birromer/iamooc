from pyibex import *
import numpy as np
from vibes import *
from pyibex.geometry import SepPolarXY

Marks = [[6,12], [-2,-5], [-3,10], [3,4]]
D = [Interval(10,13), Interval(8,10), Interval(5,7), Interval(6,8)]
Alpha = [Interval(0.5,1), Interval(-3,-1.5), Interval(1,2), Interval(2,3)]

vibes.beginDrawing()

seps = []
for m,d,alpha in zip(Marks,D,Alpha):    
    sep1 = SepPolarXY(d,alpha)
    fforw = Function("v1", "v2", "(%f-v1;%f-v2)" % (m[0],m[1]))
    fback = Function("p1", "p2", "(%f-p1;%f-p2)" % (m[0],m[1]))
    sep = SepTransform(sep1,fback,fforw)
    seps.append(sep)

sep = SepQInterProjF(seps)
sep.q = 1

P = IntervalVector([[-20, 20], [-20,20]])
vibes.newFigure('locpie')
vibes.setFigureProperties({'x':100, 'y':100, 'width':1000, 'height':700})
pySIVIA(P,sep,0.1)

for m in Marks:
    vibes.drawCircle(m[0], m[1], 0.3, 'yellow[black]')