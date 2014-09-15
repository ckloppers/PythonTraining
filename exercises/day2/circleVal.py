#!/Users/klo019/anaconda/bin/python
# Author: Corne Kloppers

isANumber = False
while not isANumber:
    number = raw_input('Please enter a number: ')
    if number.isdigit():
        isANumber = True

diameter = int(number) * 2

print 'A circle with a radius of %s cm ' \
      'has a diameter of %d cm' % (number, diameter)