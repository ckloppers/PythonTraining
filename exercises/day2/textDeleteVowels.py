
vowels = ('a', 'e', 'i', 'o', 'u')

text = raw_input('Input: ')

newstr = text
for x in vowels:
    newstr = newstr.replace(x,"")

print newstr

