import numpy as np

numbers = raw_input('Numbers: ')

numbersList = map(int, numbers.split())

npArray = np.array(numbersList)

print 'You entered:', npArray
print 'Amount of numbes:', npArray.size
print 'Sum:', npArray.sum()
print 'Max:', npArray.max()
print 'Min:', npArray.min()

print 'Prod: {:,}'.format(npArray.prod())