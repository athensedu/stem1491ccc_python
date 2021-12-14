"""
matrix
creating a matrix

by list comprehension
"""

def createMatrix1():
    #
    N, M = 4, 3
    m = [[1]*N] * M
    return m

def changeItem(matrix, rowIndex, colIndex, value):
    # EXCEPTION
    # pay attention to this
    matrix[rowIndex][colIndex] = value
    return matrix


# test
print('Create a matrix - by list comprehension')
matrix = createMatrix1()
print(matrix)
print()

print('change an item')
matrix = changeItem(matrix, 0, 0, 99)
print(matrix)
print()






