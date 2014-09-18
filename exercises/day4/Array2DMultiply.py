import numpy as np

def readMatrix(desc):
    matrix1 = []
    print desc,'Array: \n'
    while True:
        currrentRow = raw_input('')
        if len(currrentRow.strip()) == 0:
            break

        numbersList = map(int, currrentRow.split())
        matrix1.append(numbersList)

    return np.array(matrix1)

npMatrix1 = readMatrix('First')
npMatrix2 = readMatrix('Second')

print npMatrix1
print npMatrix2

mulMatrix = npMatrix1 * npMatrix2
print mulMatrix

np.savetxt('data.txt', mulMatrix, fmt='%i')

