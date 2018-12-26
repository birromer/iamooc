from vibes import *
from pyibex import *
import pyibex


class myCtc(Ctc):
    def __init__(C):
        Ctc.__init__(C,2)
    
    def contract(C,X):
        x, y = X[0], X[1]
        cx, cy, r = Interval(1,3),Interval(2,4),Interval(4,5)
        a, b = x-cx, y-cy
        a2,b2,r2 = sqr(a), sqr(b), sqr(r)
        bwd_add(r2,a2,b2) 
        bwd_sqr(a2,a)
        bwd_sqr(b2,b) 
        bwd_sub(a,x,cx)
        bwd_sub(b,y,cy)
        
    
vibes.beginDrawing()
vibes.newFigure('one ring with pyibex')
vibes.setFigureProperties({'x':200, 'y':100, 'width':800, 'height':800})
X0=IntervalVector(2, [-10,10])
ctc = myCtc()
pySIVIA(X0,ctc,0.5)