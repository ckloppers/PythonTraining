import matplotlib.pyplot as plt
import math
import numpy as np

# for angle in range(360):
#     y = math.sin(math.radians(angle))
#     a.append(y)

x = np.arange(0, 2 * math.pi, 0.1)
y = np.sin(x)

plt.plot(x, y, 'ro')
plt.show()