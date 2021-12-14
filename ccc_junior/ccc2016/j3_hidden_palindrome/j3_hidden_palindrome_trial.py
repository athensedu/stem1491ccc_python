"""
CCC 2016 Junior
Problem J3. Hidden Palindrome

status:

"""

words = 'abracadabra'

def findIndexOfChar(char, targetString):
    start = 0
    end = len(targetString)
    indexList = []
    while start <= end:
        lastIndex = targetString.find(char, start, end)
        # print(lastIndex)
        if lastIndex != -1:
            indexList.append(lastIndex)
            start = lastIndex+1
        else:
            break
    return indexList

# test
allIndex = findIndexOfChar('a', words)
# print(allIndex)

# allIndex.reverse()

maxLen = 0
for left in allIndex:
    for right in allIndex:
        if left <= right:
            substr = words[left:right+1]
            if substr == substr[::-1]:
                if len(substr) > maxLen:
                    maxLen = len(substr)
                # print(substr)

print(maxLen)

