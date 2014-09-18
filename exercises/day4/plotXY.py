import matplotlib.pyplot as plt

inFile = open('data.csv', 'r')

x = []
y = []

for line in inFile:
    lineX, lineY = line.split(',')
    x.append(lineX)
    y.append(lineY)

plt.plot(x, y)
plt.show()