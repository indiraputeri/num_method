##Modul Bagi Dua
'''Akar = bagidua(f,x1,x2,switch=0,tol=1.0e-9).
menemukan akar dari f(x)=0 dengan metode bagi dua.
nilai akar haruslah terkurung di (x1,x2).
setting switch = 1 returns akar = none if f(x) increases
saat metode berjalan
'''

from math import log, ceil
from typing import Union


def f(x): return x**3 - 10*x*x + 5
#x1 = 0.6
#x2 = 0.8
#i = 1
#x3 = 0

def bagidua(f,x1,x2,switch=0,epsilon=1.0e-9):
    f1 = f(x1)
    if f1 == 0.0: return x1
    f2 = f(x2)
    if f2 == 0.0: return x2

    #if f1*f2 > 0.0: error.err('Akar tidak terkurung di nilai tersebut')

    n: Union[int] = ceil(log(abs(x2-x1)/epsilon)/log(2.0))

    for i in range(n):
        x3 = 0.5*(x1 + x2); f3 = f(x3)
        print(i, '  ', x3, '  ', f(x3))
        if(switch == 1) and (abs(f3) > abs(f1))\
                        and (abs(f3) > abs (f2)):
            return None

        if f3 == 0.0: return x3
        if f2*f3 < 0.0: x1 = x3; f1 = f3
        else:
            x2 = x3; f2 = f3
    i = 1 + 1
    return (x1 + x2)/2.0
#Run
bagidua(f,0.6,0.8,switch=0,epsilon=1.0e-9)