import time

# Data will be stored in the data dict
data = {}

def ageNextBirthDay(age):
    return age+1

# loop and get all data
counter = 1
while True:
    name = raw_input('Please enter person '+str(counter)+'\'s name: ')
    if len(name.strip()) == 0:
        break

    age = raw_input('Please enter person '+str(counter)+'\'s age: ')

    data[name] = age
    counter += 1

# print the data out
print '\nHere are the people: '
for item in data.keys():
    print item + ' is ' + data[item]

print 'Thank you. Goodbye'