import numpy as np

a = [1,2,3,4]
b = [2,3,4,5]

a = np.array(a)
b = np.array(b)
a * b

np.array([1,2,3,4,5])

type(np.array([1,2,3,4,5]))

np.zeros(10 , dtype=int)

np.random.randint(0, 10, size= 10)
np.random.normal(10,4, (3,4))

###########################################################################

a = np.random.randint(10, size = 6)
a.ndim
a.shape
a.size
a.dtype


###########################################################################

np.random.randint(1, 10, size = 9)
np.random.randint(1, 10, size = 9).reshape(3,3)
ar = np.random.randint(1, 10, size = 9)
ar.reshape(3,3)

###########################################################################

a = np.random.randint(10, size = 10)
a[0]
a[0:5]
a[0] = 999

m = np.random.randint(10, size = (3, 5))
m[0,0]
m[1,1]
m[2,3] = 999
m[2,3] = 2.9
m[: , 0]
m[1 , :]
m[0:2, 0:3]

##############################################################################

v = np.arange(0, 30, 3)
v[1]
v[4]

catch = [1,2,3]

v[catch]

##############################################################################

v = np.array([1,2,3,4,5])

v[v<3]

#################################################################################

v = np.array([1,2,3,4,5])

v / 5

v ** 2

np.subtract(v, 5)
np.add(v, 5)
np.mean(v)
np.sum(v)
np.var(v)

a = np.array([[5, 1], [1, 3]])     ### 5*x0 + x1 = 12 , x0 + 3*x1 = 10
b = np.array([12, 10])

np.linalg.solve(a, b)

########################################################################33

#sabit tip, hızlı

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('1. boyuttaki 2.eleman: ', arr[0, 1])

import numpy as np
array = np.array([1, 2, 3, 4, 5, 6, 7])

filter_array = array % 2 == 0

new_array = array[filter_array]

print(new_array)