from vibes import *
from mybox import *
from mycontractor import *

def CinRing(x, y, cx, cy, r):
    a=x-cx
    b=y-cy
    a2=sqr(a)
    b2=sqr(b)
    r2=sqr(r)
    r2,a2,b2 = cadd(r2,a2,b2)
    a2,a = csqr(a2,a)
    b2,b = csqr(b2,b)
    x,a,cx = cadd(x,a,cx)
    y,b,cy = cadd(y,b,cy)
    return x, y
    

def sivia(X):
    if X.width() < 0.3:
        return
    vibes.drawBox(X.x.lb, X.x.ub, X.y.lb, X.y.ub, 'black[cyan]')
    X.x,X.y = CinRing(X.x,X.y, Interval(1,3), Interval(2,4), Interval(4,5))
    vibes.drawBox(X.x.lb, X.x.ub, X.y.lb, X.y.ub, '[yellow]')
    sivia(X.left())
    sivia(X.right())
    

if __name__ == "__main__":
    vibes.beginDrawing()
    vibes.newFigure('one ring')
    vibes.setFigureProperties({'x':0, 'y':0, 'width':800, 'height':500})
    X=Box(Interval(-10,10),Interval(-10,10))
    sivia(X)
    vibes.endDrawing()