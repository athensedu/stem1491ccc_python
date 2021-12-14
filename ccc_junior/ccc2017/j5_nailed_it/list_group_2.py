"""

"""

a = [1,2,3,4,5,6]


def getGroup(mylist):
    result = []
    used_index = []
    n = len(mylist)
    for i in range(n):
        for j in range(n):
            if i != j:
                if i not in used_index:
                    if j not in used_index:
                        result.append([mylist[i],mylist[j]])
                        used_index.append(i)
                        used_index.append(j)
    # print(result)
    return result

for i in range(len(a)):
    print(getGroup(a))
    b = a[:]
    a = b[1:]
    a.append(b[0])