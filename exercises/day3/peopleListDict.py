
# Data will be stored in the data dict
peopleList = []


def ageNextBirthDay(age):
    return age+1

# loop and get all data
counter = 1
while True:
    name = raw_input('Please enter person '+str(counter)+'\'s name: ')
    if len(name.strip()) == 0:
        break

    lastName  = raw_input('Please enter person '+str(counter)+'\'s lastName: ')
    age = raw_input('Please enter person '+str(counter)+'\'s age: ')

    data = {'name' : name,
            'lastname' : lastName,
            'age': age}

    peopleList.append(data)
    counter += 1

# print the data out
print '\nHere are the people: '
for person in peopleList:
    print person

print 'Thank you. Goodbye'