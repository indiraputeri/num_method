import matplotlib.pyplot as plt

from numpy import exp, arange
from pylab import meshgrid

# vector = np.vectorize(np.float)
x = arange(-5, 5, 100)
y = arange(-5, 5, 100)
# x = vector(x)
# y = vector (y)

a = 1
b = 1
c = 5
d = 1.5
k = 0.7


# def f(x, y):
# return ((b1 * b2) / (a1 ** b1 / d)(a2 ** b2 / d)) * (x ** ((b1/d)-1) * y ** ((b2/d)-1)) * (((x/a1 ** b1/d) +( y/a2 ** b2/d)) ** (d-2)) * ((((x/a1 ** b1/d) + (y/a2 ** b2/d)) ** d) + (1/d)-1) * (exp(-(x/a1 ** b1/d)+(y/a2 ** b2/d)) ** d))

def f(x, y):
    return 1 - exp(-(((x / a) ** (c / d)) + ((y / b) ** (d / k))) ** k)


X, Y = meshgrid(x, y)
Z = f(x, y)
fig = plt.figure()
ax = fig.gca(projection = '3d')
surf = ax.plot_trisurf(list(X), list(Y), list(Z), linewidth=0.2, antialiased=True)
plt.show()
