import random

# stats data structure
stats = {1:0,
         2:0,
         3:0,
         4:0,
         5:0,
         6:0}

# method to roll dice
def rollDice():
    return random.randint(1, 6)

# rolling the dice
print 'Now rolling the die...'
for roll in range(1, 10):
    currentRoll = rollDice()
    currentRollValueInDict = stats[currentRoll]
    stats[currentRoll] = currentRollValueInDict + 1

# Print out the stats
keys = stats.keys()
keys.sort()
print 'Tally is:'
for item in keys:
    print 'Number of ' + str(item) +'\'s: ' + str(stats[item])