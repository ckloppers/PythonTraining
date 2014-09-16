
numbers = []
for i in range(1, 6):
    currentNumber = raw_input('Enter number ' + str(i) + ': ')
    numbers.append(int(currentNumber))

numbers.sort()

print numbers