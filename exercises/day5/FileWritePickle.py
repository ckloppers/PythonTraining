import pickle

outFile = open('names.pkl', 'w')
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

pickle.dump(dataDict, outFile)
outFile.close()
print str(counter) + ' names written to file: ' + outFile.name

inFile = open('names.pkl', 'r')
data = pickle.load(inFile)

print data


