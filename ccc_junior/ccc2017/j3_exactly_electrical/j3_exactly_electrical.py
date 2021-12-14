"""
CCC 2017 Junior
Problem J3. Exactly Electrical

status:
Resources: 0.427s, 9.41 MB
Maximum runtime on single test case: 0.026s
Final score: 15/15 (3.0/3 points)
"""

# input
x1, y1 = input().split()
x2, y2 = input().split()
t = int(input())

#
x1 = int(x1)
y1 = int(y1)
x2 = int(x2)
y2 = int(y2)

# process
distance_min = abs(x1-x2)+abs(y1-y2)

if t >= distance_min:
    result = (t - distance_min) % 2
    if result == 0:
        print('Y')
    else:
        print('N')
else:
    print('N')


