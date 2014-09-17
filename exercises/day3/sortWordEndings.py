
def compare(first, second):
    return cmp(second[-1].lower(), first[-1].lower())

sentence = raw_input('Sentence: ')
sentenceList = sentence.split(' ')
sentenceList.sort(cmp=compare, reverse=True)

print ' '.join(sentenceList)

