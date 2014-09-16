import re

searchText = raw_input('Input text: ')
if re.search("^\\s*Corne\\s*Kloppers\\s*$", searchText):
    print 'Welcome Corne Kloppers'

