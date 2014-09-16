#!/usr/bin/python

fileName = raw_input('Input file to count lines: ')

inFile = open(fileName, 'r')

count = 0
for _ in inFile:
    count += 1

# Test comment
print 'Number of lines: '+ str(count)