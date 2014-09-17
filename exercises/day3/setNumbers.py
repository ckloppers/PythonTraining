
numbers = raw_input('Enter numbers: ')
numbersList = numbers.split(' ')

numbersSet = set(numbersList)
print ' Amount of Unique Numbers ' + str(len(numbersSet))