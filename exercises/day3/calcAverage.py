import numpy

def calcAverage(*numbers):
    return numpy.mean(numbers)

print calcAverage(1,2,4)
print calcAverage(1,2)