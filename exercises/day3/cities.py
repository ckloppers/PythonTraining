

citiesDict = {}

# loop and get all data
while True:
    inputRow = raw_input('')
    if len(inputRow.strip()) == 0:
        break

    city, country = inputRow.split(',')

    city = city.strip()
    country = country.strip()

    if country in citiesDict:
        countryList = list(citiesDict[country])
    else:
        countryList = []
    countryList.append(city)
    citiesDict[country] = countryList

# Print Cities
keys = citiesDict.keys()
keys.sort()

for key in keys:
    line = ''
    value = citiesDict[key]
    value.sort()
    for i in value:
        line = line + i + ", "
    print key + ' : ' + str(line[:-1])
