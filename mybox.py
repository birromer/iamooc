import math
from myinterval import *

class Box:
    def __init__(X, a, b):
        X.x, X.y = a, b
        
    def __repr__(X):
        return("[%f,%f] X [%f,%f]"%(X.x.lb, X.x.ub, X.y.lb, X.y.ub))
        
    def width(X):
        if X.x.isEmpty() | X.y.isEmpty():
            return -oo
        else:
            return(max(X.x.width(), X.y.width()))
            
    def left(X):
        if(X.x.width() > X.y.width()):
            return Box(X.x.left(),X.y)
        else:
            return Box(X.x, X.y.left())
        
    def right(X):
        if(X.x.width() > X.y.width()):
            return Box(X.x.right(),X.y)
        else:
            return Box(X.x, X.y.right())
        
     
        
if __name__ == "__main__":
    a = Interval(2,4)
    b = Interval(4,8)
    X = Box(a,b)
    print("X = ", X)
    print("X.left() = ", X.left())
    print("X.right() = ", X.right())