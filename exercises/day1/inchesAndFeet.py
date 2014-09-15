
print 'Inches\t\t\tFeet/Inches\t\t\t' \
      'Centimeters'

inch = 1
while inch <= 20:
    feet = inch / 12
    leftOverInches = inch % 12
    print '%6i \t\t\t %2i / %2i \t\t\t %6.2f' % (inch, feet, leftOverInches, inch*2.54)
    inch = inch + 1
