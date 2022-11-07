## Metode Naive Gaussian Elimination
'''x=gaussElimin(a,b).
menyelesaikan [a]{b}={x} dengan Naive Gauss Elimination'''

from numpy import array,dot

def gaussElimin(a,b):

#Forward elimination
    for k  in range (0, n-1):
      for i in range (k+1, n):
          if a[i, k]!=0.0:
              kons = a[i, k] / a[k, k]
              a[i, k+1:n] = a[i, k+1:n] - kons*a[k, k+1:n]
              b[i] = b[i] - kons* b[k]

              print(kons)
              print (a)
              print (b)

#Backward Substitution
    for k in range (n-1,-1,-1):
      b[k] = (b[k] - dot(a[k,k+1:n],b[k+1:n]))/a[k,k]

    return (b)


a = array([[-2,5,-1,0],
           [4,-2,1,3],
           [1,3,-5,5],
           [1,3,-5,-4]], float)
b = array([3,-7,16,34], float)
n = len(b)

x = gaussElimin(a,b)
print('jadi, nilai [x] nya adalah:')
print(x)

