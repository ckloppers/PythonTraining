

# dict containing all topics
favDict = {}
for _ in range(0, 3):
    topic = raw_input('Enter a topic: ')
    fav = raw_input('What is your fav %s: ' % topic)
    favDict[topic] = fav

for topic in favDict.keys():
    print 'You fav %s is %s' % (topic, favDict[topic])