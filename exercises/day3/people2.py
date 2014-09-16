import time

# Data will be stored in the data dict
data = {}


def ageNextBirthDay(age):
    return age+1

# loop and get all data
for counter in range(1,4):
    name = raw_input('Please enter person '+str(counter)+'\'s name: ')
    age = raw_input('Please enter person '+str(counter)+'\'s age: ')

    data[name] = age

# print the data out
print '\nHere are the people: '
for item in data.keys():
    print item + ' is ' + data[item]

print 'Thank you. Goodbye'