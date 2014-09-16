#!/Users/klo019/anaconda/bin/python
# Author: Corne Kloppers


def calcAvg(num1, num2, num3):
    return (float(num1) + float(num2) + float(num3)) / 3.0

number1 = raw_input('Please enter the first number: ')
number2 = raw_input('Please enter the second number: ')
number3 = raw_input('Please enter the third number: ')




print 'The average of these three numbers is %.2f' % calcAvg(number1, number2, number3)