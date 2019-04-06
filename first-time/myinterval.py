import math

nan = float('nan')
oo =  float('inf')

class Interval:
    def __init__(x, a, b):
        if a>b:
            x.lb, x.ub = nan, nan
        else:
            x.lb, x.ub = a, b
    
    def __repr__(x):
        return("[%f,%f]"%(x.lb, x.ub))
        
    def isEmpty(x):
        return math.isnan(x.lb)
            
    def __add__(x, y):  #overloading x + y
        return Interval(x.lb+y.lb, x.ub+y.ub)
                
    def __sub__(x, y):  #overloading  x - y
        return Interval(x.lb-y.ub, x.ub-y.lb)

    def __mul__(x,y):   #overloading  x * y
        L = [x.lb*y.lb, x.ub*y.ub, x.lb*y.ub, x.ub*y.lb]
        return Interval(min(L), max(L))
    
    def __rmul__(x,y): #overloading Z * x
        return x.__mul__(Interval(y,y))

    def __contains__(x, a):
        return (x.lb<=a<=x.ub)
    
    def __truediv__(x,y):   #overloading  x / y
        if 0 in y:
            return Interval(-oo, oo)
        return x * Interval(1/y.ub, 1/y.lb)
    
    def __and__(x,y):
        if (x.isEmpty() or y.isEmpty()):
            return Interval(1,0)
        else:
            return Interval(max(x.lb, y.lb), min(x.ub, y.ub))
        
    def __or__(x,y):
        if x.isEmpty():
            return y
        elif y.isEmpty():
            return x
        else:
            return Interval(min(x.lb, y.lb), max(x.ub, y.ub))
    
    def width(x):
        return x.ub - x.lb

    def left(x):
        return Interval(x.lb, 0.5*(x.lb+x.ub))
    
    def right(x):
        return Interval(0.5*(x.lb+x.ub), x.ub)
    
def sqr(x):
    L = [x.lb**2, x.ub**2]
    if 0 in x:
        return(Interval(0, max(L)))
    else:
        return(Interval(min(L), max(L)))

def sqrt(x):
    x = x&Interval(0,oo)
    return Interval(math.sqrt(x.lb), math.sqrt(x.ub))
    
def mini(x, y):
    return(Interval(min(x.lb, y.lb), min(x.ub, y.ub)))
    
def maxi(x, y):
    return(Interval(max(x.lb, y.lb), max(x.ub, y.ub)))

def exp(x):
    return(Interval(math.exp(x.lb), math.exp(x.ub)))

def log(x):
    if x.ub <= 0:
        return(Interval(1,0))
    elif 0 in x:
        return(Interval(-oo, math.log(x.ub)))
    else:
        return(Interval(math.log(x.lb), math.log(x.ub)))
        
def subset(x,y):
    if x.isEmpty():
        return True
    else:
        return (x.lb in y) and (x.ub in y)

def disjoint(x,y):
    return (x&y).isEmpty()
        
if __name__ == "__main__":
    x = Interval(-2, 2)
    print("x = ", x)
    print("srq(x) + 2*x - exp(x) = ",sqr(x)+2*x-exp(x))