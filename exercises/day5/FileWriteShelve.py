import shelve

dinner = shelve.open('dinner.shv', 'c')

entree = raw_input('Entree: ')
main = raw_input('main: ')
desert = raw_input('desert: ')

dinner['entree'] = entree
dinner['main'] = main
dinner['desert'] = desert

dinner.close()


inFIle = shelve.open('dinner.shv', 'r')

for key, value in inFIle.iteritems():
    print key, '->', value

inFIle.close()
