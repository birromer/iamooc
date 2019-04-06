from vibes import *
from myinterval import *


def drawtube(tmin, tmax, dt, color):
    t = tmin
    m = Interval(oo,oo)
    while t < tmax:
        x = Interval(t, t+dt)
        y = sqr(x) + 2*x - exp(x)
        vibes.drawBox(x.lb, x.ub,y.lb, y.ub, color)
        t = t+dt
        m = mini(m, y)
    return m

if __name__ == "__main__":
    vibes.beginDrawing()
    vibes.newFigure('myMinimizer')
    vibes.setFigureProperties({'x':0, 'y':0, 'width':1600, 'height':1000})
    
    m1 = drawtube(-2, 2, 0.5, '[blue]')
    print("m1 = ", m1)
    m2 = drawtube(-2, 2, 0.05, '[yellow]')
    print("m2 = ", m1)
    m2 = drawtube(-2, 2, 0.005, '[red]')
    print("m3 = ", m1)
    m1 = drawtube(-2, 2, 0.0005, '[green]')
    print("m4 = ", m1)
    vibes.endDrawing()