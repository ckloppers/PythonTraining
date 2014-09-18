import matplotlib.pyplot as plt
import numpy as np


xrange = np.arange(-10, 10, 0.2)
ylist = []

for x in xrange:
    y = x**2 - 2
    ylist.append(y)

plt.plot(xrange, np.array(ylist))
plt.show()