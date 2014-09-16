import re

name = raw_input('Name: ')
email = raw_input('Email: ')

nameList = name.split(' ')

regEx = '^' + nameList[0] + '\.' + nameList[1] + email[email.find('@'):-1]

if re.search(regEx, email, re.IGNORECASE):
    print 'Valid email, name match email address'
else:
    print 'name does not match email address'