#Program Phyton di PyCharm untuk mendapatkan akar persamaan x-cos(x)
#dengan menggunakan metode bagi dua
#dengan batas (0.6,0.8) dan toleransi error 10e-14
#program ini diadaptasi dari Andrew Dotson

from typing import Any, Union
import NumPy as np
from matplotlib.pyplot import plot, grid, show

def f(x):
    return x - np.cos(x)

def bisection(a, b, tol):

    xl = a
    xr = b
    c = 0
    while (np.abs(xl - xr) >= tol):
        print(c, '', f(c))
        c: Union[float, Any] = (xl + xr) / 2.0
        prod = f(xl) * f(c)
        if prod > 0:
            xl = c
        else:
            if prod < 0:
                xr = c
    return c



#Jalankan/RUN
nilaiakar = bisection(0.6, 0.8, 10e-14)
print("Metode bagi dua menghasilkan akar di x = ", nilaiakar)

x = np.linspace(-1,5,100)
plot(x,f(x))
grid()
show()