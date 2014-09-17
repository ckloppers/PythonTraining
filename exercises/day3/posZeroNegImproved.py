import operator as op

numbers = raw_input('Enter numbers: ')
numbersList = numbers.split(',')

stats = {'pos': 0, 'neg': 0, 'zero': 0}
print 'numList ', numbersList
for num in numbersList:
    if int(num) > 0:
        count = stats['pos'] + 1
        stats['pos'] = count
    elif int(num) < 0:
        count = stats['neg'] + 1
        stats['neg'] = count
    elif int(num) == 0:
        count = stats['zero'] + 1
        stats['zero'] = count


print ' stats: ', stats