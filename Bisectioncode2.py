from numpy import *

a = int(input("masukkan nilai a"))
b = int(input("masukkan nilai b"))

xm = (a + b) / 2;


def f(x):
    y = x ** 2 -4
    return y


if f(a) * f(b) < 0:
    while abs(f(xm)) > 0.00000001:
        if 0 < f(a) * f(xm):
            a = xm
        else:
            b = xm
        xm = (a + b) / 2
    print(xm,'',f(xm))
    print("akarnya adalah", xm)
else:
    print("interval tidak valid")
