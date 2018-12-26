from vibes import *
from pyibex import *
import pyibex

vibes.beginDrawing()
vibes.newFigure('one ring with pyibex')
vibes.setFigureProperties({'x':200, 'y':100, 'width':800, 'height':800})
X0=IntervalVector([[-10,10], [-10,10]])
r=Interval(4,5)
f=Function("x1", "x2", "(x1-[1,1.3])^2+(x2-[2,2.3])^2")
sep = SepFwdBwd(f,sqr(r))
ctc=CtcFwdBwd(f,sqr(r))
pySIVIA(X0,sep,0.1)
vibes.axisEqual()