"""
matrix
creating a matrix

by list comprehension
changing a row
"""

def createMatrix1():
    N, M = 4, 3
    # shallow copy
    m = [[1]*N] * M
    return m

def changeRow2(matrix, rowNum):
    # OK
    # completely change this row
    matrix[rowNum] = [9,9,9,9]
    return matrix

def changeRow1(matrix, rowNum):
    # OK
    # all related rows are affected
    matrix[rowNum].append('x')
    return matrix

# test
print('Create a matrix - by list comprehension')
matrix = createMatrix1()
print(matrix)

print('Change a row')
matrix = changeRow1(matrix,0)
print(matrix)

print('Change a row')
matrix = changeRow2(matrix,0)
print(matrix)









