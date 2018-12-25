from vibes import *
from mybox import *

def test(P):
    b = Interval(0,0)
    for i in range(len(Y)):
        ti, Yi = T[i], Y[i]
        Fi = P.x*exp(ti*P.y)
        if subset(Fi,Yi):
            b.lb=b.lb+1
        if not(disjoint(Fi,Yi)):
            b.ub=b.ub+1
    return b

def sivia(P):
    vibes.selectFigure('P')
    b = test(P)
    q = 0
    if b.ub < len(Y)-q:
        vibes.drawBox(P.x.lb, P.x.ub, P.y.lb, P.y.ub, '[cyan]')
    elif b.lb >= len(Y)-q:
        vibes.drawBox(P.x.lb, P.x.ub, P.y.lb, P.y.ub, '[red]')
    elif P.width() < 0.01:
        vibes.drawBox(P.x.lb, P.x.ub, P.y.lb, P.y.ub, 'yellow[yellow]')
        DrawOutput(P)
    else:
        sivia(P.left())
        sivia(P.right())
        
def DrawOutput(P):
    t, dt = 0, 0.05
    vibes.selectFigure('Y')
    while t < 5:
        T = Interval(t, t+dt)
        y = P.x*exp(t*P.y)
        vibes.drawBox(T.lb, T.ub, y.lb, y.ub, 'green[green]')
        t=t+dt



if __name__ == "__main__":
    vibes.beginDrawing()
    vibes.newFigure('P')
    vibes.setFigureProperties({'x':0, 'y':0, 'width':800, 'height':500})
    vibes.newFigure('Y')
    vibes.setFigureProperties({'x':700, 'y':0, 'width':800, 'height':500})
        
    T = [0.2, 1, 2, 4]
    Y = [Interval(1.5,2), Interval(0.7,0.8), Interval(0.1,0.3), Interval(-0.1,0.03)]    
    P = Box(Interval(-3,3), Interval(-3,3))
    sivia(P)
    vibes.selectFigure('Y')
    for i in range(len(Y)):
        vibes.drawBox(T[i]-0.01, T[i]+0.01, Y[i].lb, Y[i].ub, 'red[red]')
    

    vibes.endDrawing()