import re


fileName = raw_input('File name: ')

inFile = open(fileName, 'r')

for line in inFile:
    if line.startswith('#') and not re.match('#!', line):
        print line.strip()