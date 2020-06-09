import numpy as np
# a = np.arange(3)
# print(a.shape, a.ndim)
# print(a)
# a1 = a.reshape(1,3)
# print(a1.shape, a1.reshape)

# a2 = np.swapaxes(a1, 0, 1)
# print(a2)
# print(a2.shape, a2.ndim)

# a3 = np.arange(6).reshape(1,2,3)
# print(a3)
# print(a3.shape, a3.ndim)
# print(a3)

# a4 = np.swapaxes(a3,1,2)
# print(a4)
# print(a4.shape, a4.ndim)

# a5 = np.swapaxes(a3, 0,1)
# print(a5.shape, a5.ndim)

# a6 = np.arange(6).reshape(2,3)
# print(a6)

# a7 = a6.T
# print(a7)

# a6 = np.array(6).reshape(1,2,3)
# print(a6)
# print("")

# a7 = np.transpose(a6,(1,0,2))
# a8 = np.transpose(1,0,2)
# print(a7)
# print(a8)
# a9 = np.transpose(a6, (1, 0))
# print(a9)
# print(a6)

import random
from matplotlib import pyplot as plt

position = 0 
walk = [position]
steps = 1000
for i in range(steps):
    step = 1 if random.randint(0,1) else -1
    position += step
    walk.append(position)

plt.plot(walk[:100])
