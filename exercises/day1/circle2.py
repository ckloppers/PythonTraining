#!/Users/klo019/anaconda/bin/python
# Author: Corne Kloppers


radius = float(raw_input('Please enter a number: '))
PIE = 3.141593
diameter = radius * 2
circumference = 2 * PIE * radius
area = PIE * radius ** 2
volume = 4.0/3.0 * PIE * (radius ** 3)


print """
      A circle with a radius of %s cm
      has a diameter of %d cm
      a circumference of %f cm
      and an area of %f cm square
      and volume of %f """ % (radius, diameter, circumference, area, volume)