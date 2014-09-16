#!/Users/klo019/anaconda/bin/python
# Author: Corne Kloppers


import math as m

radius = float(raw_input('Please enter a number: '))
PIE = m.pi
diameter = radius * 2
circumference = 2 * PIE * radius
area = PIE * radius ** 2
volume = 4.0/3.0 * PIE * (radius ** 3)




print 'PI: ',PIE
print 'A circle with a radius of %6.2f cm ' % radius
print 'has a diameter of         %6.2f cm ' % diameter
print 'a circumference of        %6.2f cm ' % circumference
print 'and an area of            %6.2f cm square' % area
print 'and volume of             %6.2f ' % volume