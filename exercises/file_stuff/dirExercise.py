import os

if not os.path.isdir('Life'):
    os.mkdir('Life')
os.chdir('Life')
outFile = open('TheMeaningOfLife.txt', 'w')

outFile.write("""
    Well, it's sd;sdgdfs
    sgd
    sdf
    sd


    dfghdfghdfghdfghdf
    sdgdfgsdf
""")

os.rename('TheMeaningOfLife.txt', 'TheMeaningOfLife.bak'
                                  '')

