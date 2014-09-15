
def printFriends(friendList):
    print 'Your friends are: '
    count = 1
    for name in friendList[:-1]:
        print str(count) +'. ' + name
        count = count + 1


moreFriends = True
friendList = []

while moreFriends:
    if not moreFriends:
        break
    friend = raw_input('Please enter your friends: ')
    friendList.append(friend)
    if len(friend.strip()) == 0:
        moreFriends = False


print 'You have %d friends ' % ( len(friendList) - 1 )

printFriends(friendList)

newFriend =  raw_input('Enter your new friend: ')
position = raw_input('What position should %s be in: ' % newFriend)

friendList.insert(int(position)-1, newFriend)

printFriends(friendList)

toRevoke = raw_input('FriendToRevoke: ')

friendList.pop(int(toRevoke)-1)

printFriends(friendList)
