from mycontractor import *


if __name__ == "__main__":
    R1 = Interval(0,oo)
    R2 = Interval(0,oo)
    R = Interval(-oo,oo)
    E = Interval(23,26)
    I2 = Interval(-oo,oo)
    I = Interval(4,8)
    U1 = Interval(10, 11)
    U2 = Interval(14, 17)
    P = Interval(124, 130)
    print("R1 = ", R1, " R2 = ", R2, " E= ", E, " I = ", I, " U1= ", U1, " U2 = ", U2, " I2 = ", I2)
    for k in range(0,10):
        R,R1,R2 = cadd(R,R1,R2)
        P,E,I = cmul(P,E,I)
        E,R,I = cmul(E,R,I)
        U2,R2,I = cmul(U2,R2,I)
        U1,R1,I = cmul(U1,R1,I)
        E,U1,U2 = cadd(E,U1,U2)
        I2,I = csqr(I2,I)
        P,R,I2 = cmul(P,R,I2)
    print("R1 = ", R1, " R2 = ", R2, " E= ", E, " I = ", I, " U1= ", U1, " U2 = ", U2, " I2 = ", I2)
 