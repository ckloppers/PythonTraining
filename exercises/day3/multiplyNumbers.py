def multiPlyNumbers(a, b):
    return a * b

numbers = raw_input('numebers: ')

numbersList = numbers.split(',')
intNumList = map(int, numbersList)

print reduce(multiPlyNumbers, intNumList)

