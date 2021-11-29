"""
flipping matrix
"""
def printMatrix(m):
    for row in m:
        print(row)

matrix =[[0,1,2,3],
         [9,0,2,3],
         [9,9,0,3],
         [9,9,9,0]]

printMatrix(matrix)

N = 4
for row in range(N):
    for col in range(N):
        if row < col:
            print(row, col)
            matrix[col][row]=matrix[row][col]


printMatrix(matrix)


