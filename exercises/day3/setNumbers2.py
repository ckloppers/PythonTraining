
numbers = raw_input('Enter numbers: ')
numbersList = numbers.split(' ')

numbersSet = set(numbersList)

if ('1' in numbersSet) and ('2' in numbersSet) and ('3' in numbersSet):
    print ' 1, 2, 3 in list '
else:
    print '1,2,3 not in list'