import re

searchText = raw_input('Input text: ')
if re.search("^Hi", searchText):
    print 'Welcome'