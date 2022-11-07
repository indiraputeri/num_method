import numpy

a = numpy.array([[-2, 5, -1, 0],
                 [4,-2,1,3],
                 [1,3,-5,5],
                 [1,3,-5,-4]], float)
b = numpy.array([3, -7, 16, 34], float)
n = len(b)
x = numpy.zeros(n, float)

print(a)
print(b)
print ('')

# langkah 1: Eliminasi
for k in range(n - 1):
    for i in range(k + 1, n):
        if a[i, k] == 0: continue
        konstanta = a[i, k] / a[k, k]
        for j in range(k, n):
            a[i, j] = a[i, j] - a[k, j] * konstanta
        b[i] = b[i] - b[k] * konstanta
        print('')
        print(konstanta)
        print(a)
        print(b)

print ('')
print('Jadi, matriks diagonal atas adalah sbb:')
print(a)
print(b)

# Langkah 2: Substitusi
x[n-1] = b[n-1] / a[n-1, n-1]
for i in range(n - 2,-1,-1):
    sum_ax = 0
    for j in range(i + 1, n):
        sum_ax += a[i,j] * x[j]
    x[i] = (b[i]-sum_ax) / a[i, i]

print('')
print('Solusi dari sistem persamaan ini adalah')
print('{x}=', x)
