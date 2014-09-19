import numpy as np
import matplotlib.pyplot as plt

xrange = np.arange(-12.5, 12.5)
ylist = []

for x in xrange:
    y = (2 * x**3) - (3 * x**2) - (144 * x) + 432
    ylist.append(y)

plt.plot(xrange, np.array(ylist))
plt.savefig('fig.svg')
plt.show()