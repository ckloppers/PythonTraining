import math as m

angle = raw_input('Please entet an angle: ')

print 'For an angle of %s degrees, the:' % angle
print 'sine is: %6.2f' % m.sin(m.radians(float(angle)))
print 'cosine is: %6.2f' % m.cos(m.radians(float(angle)))
print 'tangent is: %6.2f' % m.tan(m.radians(float(angle)))