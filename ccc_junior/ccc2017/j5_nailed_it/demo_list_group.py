"""
grouping
"""


mylist = [1,1,2,2]
for i in range(len(mylist)):
    s = []
    for i in range(0, len(mylist),2):
        b = mylist[i:i+2]
        b.sort()
        s.append(b)
        s.sort()
    print(s)
    newlist = mylist[:]
    mylist = newlist[1:]
    mylist.append(newlist[0])
    # print(mylist)

