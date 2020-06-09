import numpy as np
x = np.random.randint(100, size =10)
print(x)

print(x[3], x[7], x[2])
print(x[[3,7,2]])
index =[ 3,7,2]
print(x[index])

x2 = np.arange(12).reshape((3,4))
print(x2)
row = np.array([0,1,2])
col = np.array([2,1,3])
print(x2[row, col])

x3 = np.random.rand(6)
print(x3)
x4 = np.random.rand(3,2)
print(x4)
