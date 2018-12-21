import math
from myinterval import *

def cadd(z,x,y): #contractor for addition  Z = X + Y
    return z&x+y, x&z-y, y&z-x

def cmul(z, x, y): #z =x*y
    return z&x*y, x&z/y, y&z/x

def cexp(y, x): #y=exp(x)
    return y&exp(x), x&log(y)

def csqr(y, x):
    x1 = x&Interval(-oo,0)
    x2 = x&Interval(0,oo)
    y = (y&sqr(x1)) | (y&sqr(x2))
    if y.isEmpty():
        return y,y
    else:
        x1 = x1&(-1*sqrt(y))
        x2 = x2&(sqrt(y))
        return y, x1|x2

if __name__ == "__main__":
    a = Interval(-1,2)
    b = Interval(3,4)
    c = Interval(5,20)
    print("a = ", a, " b = ", b)
    b,a = csqr(b, a)
    print("a = ", a, " b = ", b)
    