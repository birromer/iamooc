from pyibex import *
from vibes import *
f = Function('x', 'y', 'x*cos(x-y)+y')
sep = SepFwdBwd(f, CmpOp.LEQ)
X0 = IntervalVector(2, [-10, 10] )
vibes.beginDrawing()
pySIVIA(X0, sep, 0.1)
vibes.saveImage('helloIntervals.jpg')
vibes.endDrawing()