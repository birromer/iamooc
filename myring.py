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
    
    return x, y
    





if __name__ == "__main__":
    