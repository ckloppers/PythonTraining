

def addLists(list1, list2):
    result = []

    for i in range(0, len(list1)):
        result.append(list1[i] + list2[i])

    return result

list1 = [1, 2, 3]
list2 = [4, 5, 6]

print addLists(list1, list2)