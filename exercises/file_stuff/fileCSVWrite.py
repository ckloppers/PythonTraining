
outFile = open('names.cvs', 'w')
# write header
outFile.write("Name,Phone\n")


getMoreData = True
counter = 1
while getMoreData:
    name = raw_input('Please enter person ' + str(counter) + '\'s name: ')
    if len(name.strip()) == 0:
        getMoreData = False
        break
    phone = raw_input('Please enter person ' + str(counter) + '\'s phone: ')

    lineToWrite =  name + "," + phone + "\n"
    outFile.write(lineToWrite)
    counter += 1

outFile.close()
print str(counter) + ' names written to file: ' + outFile.name