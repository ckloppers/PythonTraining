

def calculateAve(list):
    total = 0
    for item in list:
        total = total + item

    return (total / len(list))

def calculateTotal(list):
    total = 0
    for item in list:
        total = total + item
    return total

def calNegativeNums(list):
    total = 0
    for item in list:
        if item < 0:
            total = total + 1
    return total

def calPosNums(list):
    total = 0
    for item in list:
        if item > 0:
            total = total + 1
    return total

def calZeroNums(list):
    total = 0
    for item in list:
        if item == 0:
            total = total + 1
    return total

numberDict = {}
print 'Please enter ten numbers: '
for count in range(0, 10):
    numberDict[count] = float(raw_input())


print 'Statistics'
print '-'*20
print 'Total:', str(calculateTotal(numberDict.values()))
print 'Ave:', str(calculateAve(numberDict.values()))

print 'Number of positive: ', str(calPosNums(numberDict.values()))
print 'negatives: ', str(calNegativeNums(numberDict.values()))
print 'zero: ', str(calZeroNums(numberDict.values()))

print 'Max: ', max(numberDict.values())
print 'Min: ', min(numberDict.values())