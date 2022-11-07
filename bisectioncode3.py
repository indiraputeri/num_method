def f(x):
    y = x ** 3 - 3 * x + 1
    return y


a = 1.
b = 10.
c = (a + b) / 2

while abs(f(c)) < 0.000001:
    print(c, ' ', f(c))
    if f(a) * f(b) > 0:
        a = c
    else:
        b = c

    c = (a + b) / 2



print ("akar dari persamaan adalah: ",c)
