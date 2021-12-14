"""
CCC 2017 Junior
Problem J2. Shifty Sum

status:
Resources: 0.378s, 9.31 MB
Maximum runtime on single test case: 0.026s
Final score: 15/15 (3.0/3 points)
"""

# input
N = int(input())
K = int(input())

# process
sum = 0
for i in range(K+1):
    sum = sum + N
    N = N *10

# output
print(sum)
