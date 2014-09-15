#!/Users/klo019/anaconda/bin/python
# Author: Corne Kloppers


name = raw_input("Please enter your name: ")
age = raw_input("Please enter your age: ")

ageNotOkay = True
while ageNotOkay:
    if 0 < int(age) < 120:
        ageNotOkay = False
        break
    print 'your age should be between 0 and 120, please try again.'
    age = raw_input("Please enter your age: ")


print "Hello", name
print "Gee, you are only", age
