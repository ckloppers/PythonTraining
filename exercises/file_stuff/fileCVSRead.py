inFile = open('names.cvs', 'r')

# Dump header
inFile.readline()
for line in inFile:
    name, number = line.strip().split(',')
    print name + '\'s phone number is ' + number