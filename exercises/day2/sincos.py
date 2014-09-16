import math as m

angle = raw_input('Please entet an angle: ')

print 'For an angle of %s degrees, the:' % angle
print 'sine is: ', m.sin(m.radians(float(angle)))
print 'cosine is: ',m.cos(m.radians(float(angle)))
print 'tangent is: ',m.tan(m.radians(float(angle)))