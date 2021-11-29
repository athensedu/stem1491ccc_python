"""

"""

def rotateLeft(matrix):
    matrix[:] = map(list, zip(*matrix))
    return matrix[::-1]

def rotateRight(matrix):
    matrix[:] = map(list, zip(*matrix[::-1]))
    return matrix

def printMatrix(m):
    for row in m:
        print(row)

matrix =[[0,1,2,3],
         [9,0,2,3],
         [9,8,0,3],
         [9,7,6,0]]

printMatrix(matrix)
print()

m = rotateRight(matrix)
printMatrix(m)
print()

m = rotateLeft(matrix)
printMatrix(m)