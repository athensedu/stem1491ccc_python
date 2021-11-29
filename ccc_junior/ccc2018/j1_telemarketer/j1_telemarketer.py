"""
J1. Telemarketer

Resources: 0.376s, 9.23 MB
Maximum runtime on single test case: 0.025s
Final score: 15/15 (3.0/3 points)
"""

# 1st digit is 8 or 9
# last digit is 8 or 9
# 2nd char = 3rd digit

d1 = input()
d2 = input()
d3 = input()
d4 = input()

if d1 in ('8','9') and d4 in ('8','9') and d2 == d3:
    print("ignore")
else:
    print("answer")

