#!/Users/klo019/anaconda/bin/python
# Author: Corne Kloppers

import circleFn as cF

radius = float(raw_input('Please enter a number: '))
diameter = cF.calcDiameter(radius)
circumference = cF.calcCircumference(radius)
area = cF.calcArea(radius)
volume = cF.calVolume(radius)


print 'A circle with a radius of %6.2f cm ' % radius
print 'has a diameter of         %6.2f cm ' % diameter
print 'a circumference of        %6.2f cm ' % circumference
print 'and an area of            %6.2f cm square' % area
print 'and volume of             %6.2f ' % volume