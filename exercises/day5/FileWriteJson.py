import json

outFile = open('names.json', 'w')
# write header

counter = 1

dataDict = {}

while True:
    name = raw_input('Please enter person ' + str(counter) + '\'s name: ')
    if len(name.strip()) == 0:
        break
    phone = raw_input('Please enter person ' + str(counter) + '\'s phone: ')

    dataDict[name+phone] = (name, phone)
    counter += 1

json.dump(dataDict, outFile)
outFile.close()
print str(counter) + ' names written to file: ' + outFile.name

inFile = open('names.json', 'r')
data = json.load(inFile)

print data


