from vibes import *
from pyibex import *
import pyibex

vibes.beginDrawing()
vibes.newFigure('one ring with pyibex')
vibes.setFigureProperties({'x':200, 'y':100, 'width':800, 'height':800})
X0=IntervalVector([[-10,10], [-10,10]])

f1 = Function("x[2]", "(x[0]-1)^2+(x[1]-2)^2")
f2 = Function("x[2]", "(x[0]-2)^2+(x[1]-5)^2")

sep1 = SepFwdBwd(f1, sqr(Interval(4,5)))
sep2 = SepFwdBwd(f2, sqr(Interval(5,6)))
#sep=sep1&sep2
sep=sep1|sep2
pySIVIA(X0,sep,0.1)
vibes.axisEqual()