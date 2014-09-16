#!/Users/klo019/anaconda/bin/python
# Author: Corne Kloppers

import math

def calcDiameter(radius):
    return radius * 2

def calcCircumference(radius):
    return 2 * math.pi * radius

def calcArea(radius):
    return math.pi * radius ** 2

def calVolume(radius):
    return 4.0/3.0 * math.pi * (radius ** 3)

radius = float(raw_input('Please enter a number: '))
diameter = calcDiameter(radius)
circumference = calcCircumference(radius)
area = calcArea(radius)
volume = calVolume(radius)


print 'A circle with a radius of %6.2f cm ' % radius
print 'has a diameter of         %6.2f cm ' % diameter
print 'a circumference of        %6.2f cm ' % circumference
print 'and an area of            %6.2f cm square' % area
print 'and volume of             %6.2f ' % volume