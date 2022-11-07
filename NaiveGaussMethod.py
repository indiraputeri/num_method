from numpy import array, zeros

a = array([[6,-2,2,4], [12,-8,6,10], [3,-13,9,3], [-6,4,1,-18]], float)
b = array([16,26,-19,-34], float)

n = len(b)
x = zeros(n, float)

print(a)
print(b)
print('')

#Langkah 1: Eliminasi

for k in range(n-1):
    for i in range(k + 1, n):
        if a[i, k] == 0.0: continue
        kons = a[i, k]/a[k, k]
        for j in range(k, n):
            a[i, j] = a[i, j] - a[k, j] * kons
        b[i] = b[i] - b[k] * kons

        print('')
        print(kons)
        print(a)
        print(b)

print('')
print('Jadi, matriks diagonal atas yang terbentuk adalah sbb:')
print(a)
print(b)

# Langkah 2: Substitusi
x[n-1] = b[n-1] / a[n-1, n-1]
for i in range(n-2,-1,-1):
    sum_ax = 0
    for j in range(i + 1, n):
        sum_ax = sum_ax +  a[i,j] * x[j]
    x[i] = (b[i] - sum_ax) / a[i, i]

print('')
print('Solusi dari sistem persamaan ini adalah:')
print('{x} = ',x)
