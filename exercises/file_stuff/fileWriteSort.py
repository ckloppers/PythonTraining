
outFile = open('names.cvs', 'w')
# write header
outFile.write("Name,Phone\n")

counter = 1

dataDict = {}

while True:
    name = raw_input('Please enter person ' + str(counter) + '\'s name: ')
    if len(name.strip()) == 0:
        break
    phone = raw_input('Please enter person ' + str(counter) + '\'s phone: ')

    dataDict[name+phone] = (name, phone)
    counter += 1

# Sort Keys
keys = dataDict.keys()
keys.sort()

# write sorted keys to file
for key in keys:
    lineToWrite =  dataDict[key][0] + "," +  dataDict[key][1] + "\n"
    outFile.write(lineToWrite)

outFile.close()
print str(counter) + ' names written to file: ' + outFile.name