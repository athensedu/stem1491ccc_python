"""
CCC 2016 Junior
Problem J3. Hidden Palindrome

status:
Resources: 0.203s, 9.14 MB
Maximum runtime on single test case: 0.026s
Final score: 15/15 (5.0/5 points)
"""

def findIndexOfChar(char, targetString):
    start = 0
    end = len(targetString)
    indexList = []
    while start <= end:
        lastIndex = targetString.find(char, start, end)
        if lastIndex != -1:
            indexList.append(lastIndex)
            start = lastIndex+1
        else:
            break
    return indexList

# main
words = input()
maxLen = 0

for char in words:
    allIndex = findIndexOfChar(char, words)

    for left in allIndex:
        for right in allIndex:
            if left <= right:
                # get possible substring only
                substr = words[left:right+1]

                # check if it is palindrome
                if substr == substr[::-1]:
                    if len(substr) > maxLen:
                        maxLen = len(substr)

print(maxLen)