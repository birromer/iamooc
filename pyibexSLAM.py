from pyibex import *
from vibes import *
import numpy as np
import random
import math

def rand(I):
    x=I.lb() + random.random()*(I.ub()-I.lb())
    return x

def cstate(x1,y1,x,y,th):
    fx = Function("x1", "x", "th", "x1-x-%f*10*cos(th)" % dt)
    fy = Function("y1", "y", "th", "y1-y-%f*10*sin(th)" % dt)
    Cx = CtcFwdBwd(fx,Interval(0,0))
    Cy = CtcFwdBwd(fy,Interval(0,0))

    Bx = IntervalVector(3)
    Bx[0],Bx[1],Bx[2] = x1,x,th
    Cx.contract(Bx)
    x1,x,th = Bx[0],Bx[1],Bx[2]

    By = IntervalVector(3)
    By[0],By[1],By[2] = y1,y,th
    Cy.contract(By)
    y1,y,th = By[0],By[1],By[2]

    return x1,y1,x,y


def cmarks(x,y,mx,my,d):
    f = Function("x", "y", "mx", "my", "(x-mx)^2 + (y-my)^2")
    C = CtcFwdBwd(f, sqr(d))

    X = IntervalVector(4)
    X[0],X[1],X[2], X[3] = x,y,mx,my
    C.contract(X)
    x,y,mx,my = X[0],X[1],X[2], X[3]

    return x,y,mx,my


vibes.beginDrawing()
vibes.newFigure('SLAM')
vibes.setFigureProperties({'x':100, 'y':100, 'widht':1400, 'height':700})


_x, _y, _th, dt = 0, 0, 1, 0.1
_X, _Y = [_x], [_y]
Th, J, D = [], [], []
_mx, _my = [6,-2,-3,3], [1,-5,4,4]

noise = 0.03*Interval(-1,1)
kmax = 100
for k in range(0,kmax):
    j = random.randint(0,3)   #selects randomly the mark that will be seen by the robot
    J.append(j)
    _d = np.sqrt((_mx[j]-_x)**2 + (_my[j]-_y)**2)
    D.append(_d+rand(noise)+noise)
    _X.append(_x)
    _Y.append(_y)
    Th.append(_th+rand(noise)+noise)
    _x = _x+dt*10*np.cos(_th)
    _y = _y+dt*10*np.sin(_th)
    _th = _th+dt*(3*np.sin(k*dt)**2+rand(noise))

X = [Interval(-20,20)]*(kmax+1)
X[0] = Interval(0)
Y=X.copy()
Mx = [Interval(-20,20)]*4
My = [Interval(-20,20)]*4

for n in range(0,5):
    for k in range(1,kmax):
        X[k], Y[k], X[k-1], Y[k-1] = cstate(X[k], Y[k], X[k-1], Y[k-1], Th[k-1])
    for k in range(kmax,1,-1):
        X[k], Y[k], X[k-1], Y[k-1] = cstate(X[k], Y[k], X[k-1], Y[k-1], Th[k-1])
    for k in range(0,kmax):
        j = J[k]
        X[k], Y[k],Mx[j], My[j] = cmarks(X[k], Y[k],Mx[j], My[j], D[k])

    for Xk,Yk in zip(X,Y):
        vibes.drawBox(Xk[0],Xk[1],Yk[0],Yk[1], 'blue[cyan]')

    for j in range(0,4):
        vibes.drawBox(Mx[j][0], Mx[j][1], My[j][0], My[j][1], 'magenta[]')

for Xk,Yk in zip(X,Y):
    vibes.drawBox(Xk[0],Xk[1],Yk[0],Yk[1], 'blue[black]')

for j in range(0,4):
    vibes.drawBox(Mx[j][0], Mx[j][1], My[j][0], My[j][1], 'red[red]')

for j in range(0,4):
    vibes.drawCircle(_mx[j], _my[j], 0.06, 'black[magenta]')

for k in range(0,kmax):
    vibes.drawCircle(_X[k], _Y[k], 0.03, 'black[black]')
