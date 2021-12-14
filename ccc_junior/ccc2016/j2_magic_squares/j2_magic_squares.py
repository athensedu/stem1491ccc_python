"""
CCC 2016 Junior
Problem J2. Magic Squares

status:
Resources: 0.303s, 9.36 MB
Maximum runtime on single test case: 0.026s
Final score: 15/15 (3.0/3 points)
"""

# input
N = 4
squares = []
for i in range(N):
    row = input().split()
    row = list(map(int, row))
    squares.append(row)

# print(squares)

# sum of row
sumset = set()
for row in squares:
    sum = 0
    for i in range(N):
        sum += row[i]
    sumset.add(sum)

if len(sumset)>1:
    print('not magic')

else:
    # sum of
    vsquares = list(zip(*squares))
    vsumset = set()
    for row in squares:
        sum = 0
        for i in range(N):
            sum += row[i]
        sumset.add(sum)

    if len(vsumset)>1:
        print('not magic')
    else:
        print('magic')

