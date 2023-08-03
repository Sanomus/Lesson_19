import numpy as np

size = (4, 3)
print(type(size))
a = np.zeros(size)
print(a)

b = np.ones(size)
print(b)
c = np.ones(size)
print(c)
d = np.arange(12)
print(d.reshape((4, 3)))

ar = np.arange(100)
ar2 = 2*ar ** 2 + 5
print(ar)
print(ar2)

ar = np.arange(-10,10 )
ar2 = np.e**-ar 
print(ar)
print(ar2)