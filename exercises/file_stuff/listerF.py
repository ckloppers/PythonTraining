import os

fileList = os.listdir('.')

for filename in fileList:
    stats = os.stat(filename)
    if (stats.st_size > 1024):
        print filename + ' fileSize: ' + str(stats.st_size)+'B'