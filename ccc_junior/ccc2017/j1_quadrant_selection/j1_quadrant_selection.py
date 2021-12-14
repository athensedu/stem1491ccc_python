"""
CCC 2017 Junior
Problem J1. Quadrant Selection

status:
Resources: 0.376s, 9.36 MB
Maximum runtime on single test case: 0.025s
Final score: 15/15 (3.0/3 points)
"""

# input
x = int(input())
y = int(input())

# process
if x>0 and y>0:
    print(1)
elif x<0 and y>0:
    print(2)
elif x<0 and y<0:
    print(3)
elif x>0 and y<0:
    print(4)
else:
    pass

