import re

searchText = raw_input('Input text: ')
if re.search("Corne", searchText, re.I):
    print 'Welcome corne'