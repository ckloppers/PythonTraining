
tupleMethods = dir(tuple)
listMethods = dir(list)

print set(tupleMethods).intersection(set(listMethods))

