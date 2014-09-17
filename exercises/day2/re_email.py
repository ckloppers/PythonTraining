import re

name = raw_input('Name: ')
email = raw_input('Email: ')

nameList = name.split(' ')

regEx = '^[\w\-.]+@[\w\-]+(\.[\w-]+){1,100}'

if re.search(regEx, email, re.IGNORECASE):
    print 'Valid email, name match email address'
else:
    print 'Not a valid email address'