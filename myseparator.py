from vibes import *
from mybox import *
from mycontractor import *
from myring import CinRing

def SinRing(x, y, cx, cy, r, outer):
    if outer: #returns classical contractor
        x, y = CinRing(x, y, cx ,cy, r)
        return x,y
    else: #returns complementary set
        xa, ya = x, y #in relation to the inner ring
        xb, yb = x, y # in relation to the outer ring
        xa, ya = CinRing(xa, ya, cx, cy,Interval(0,r.lb)) #contraction correspondent to the disk
        xb, yb = CinRing(xb, yb, cx, cy,Interval(r.ub,oo)) #contraction correspondent to the outer ring
        x, y = xa|xb, ya|yb
    return x, y #returns only 1 box, has to call with two values for outer to get both options

def Sep(x, y, outer):
    cx1, cy1, r1 = Interval(1, 1), Interval(2, 2), Interval(4, 5)
    cx2, cy2, r2 = Interval(2, 2), Interval(5, 5), Interval(5, 6)
    x1, y1 = x,y
    x2, y2 = x,y
    x1, y1 = SinRing(x1, y1, cx1, cy1, r1, outer)
    x2, y2 = SinRing(x2, y2, cx2, cy2, r2, outer)
    if outer:
        x, y = x1|x2, y1|y2
    else:
        x, y = x1&x2, y1&y2
    return x, y

def sivia(X):
    if X.width() < 0.1:
        return
    vibes.drawBox(X.x.lb, X.x.ub, X.y.lb, X.y.ub, 'black[cyan]')
    X.x, X.y = Sep(X.x, X.y, True)
    vibes.drawBox(X.x.lb, X.x.ub, X.y.lb, X.y.ub, 'red[magenta]')
    X.x, X.y = Sep(X.x, X.y, False)
    vibes.drawBox(X.x.lb, X.x.ub, X.y.lb, X.y.ub, '[yellow]')
    sivia(X.left())
    sivia(X.right())


if __name__ == "__main__":
    vibes.beginDrawing()
    vibes.newFigure('one ring')
    vibes.setFigureProperties({'x':0, 'y':0, 'width':800, 'height':500})
    X = Box(Interval(-10, 10), Interval(-10, 10))
    sivia(X)
    vibes.endDrawing()
