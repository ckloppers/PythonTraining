import re

searchText = raw_input('Input text: ')
if re.search(".*a.*e.*i.*o.*u.*", searchText):
    print 'All vowels found in order'