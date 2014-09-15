import math

def FindAllDivisors(x):
    divList = []
    y = 1
    while y <= math.sqrt(x):
        if x % y == 0:
            divList.append(y)
            divList.append(int(x / y))
        y += 1
    return sorted(divList)

number = raw_input('Number: ')
print 'Divisors: ', FindAllDivisors(int(number))
