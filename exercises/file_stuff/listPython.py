import os, re


numberOfProg = 0
numberWithComments = 0
totalComments = 0

def countComments(fileName):
    inFile = open(fileName, 'r')

    count = 0
    for line in inFile:
        if line.startswith('#') and not re.match('#!', line):
            count += 1
    return count


def testForComments(fileName):
    inFile = open(fileName, 'r')

    for line in inFile:
        if line.startswith('#') and not re.match('#!', line):
            return True
    return False

fileNames = os.listdir('.')

for fileName in fileNames:
    if fileName.endswith('.py'):
        numberOfProg += 1
        if testForComments(fileName):
            numberWithComments += 1
            amountOfComments = countComments(fileName)
            totalComments += amountOfComments
            print fileName + ' number of comments: '+str(amountOfComments)
        else:
            print fileName + ' No comments found'


print '\nStats'
print '-'*20

print 'Number of programs: '+str(numberOfProg)
print 'Number of programs with comments: '+str(numberWithComments)
print 'Total number of comments: '+str(totalComments)