"""
Circle Function Module

"""
import math

def calcDiameter(radius):
    """
    Calculate the radius

    """
    return radius * 2

def calcCircumference(radius):
    """
    Calculate Circumference

    """
    return calcDiameter(radius) * math.pi

def calcArea(radius):
    """
    Calculate Area

    """
    return math.pi * radius ** 2

def calVolume(radius):
    """
    Calculate volume

    """
    return 4.0/3.0 * math.pi * (radius ** 3)

def main():
    print 'main method'

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  main()
