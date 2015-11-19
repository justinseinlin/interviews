#! /usr/bin/python
#####################################################
# Given a 1D array of integers, write sum(x, y) that
# returns the sum of integers from x-th to y-th indices
# inclusive in O(1) time.
#####################################################

sumArr = []
def primeSumArr():
    currSum = 0
    for elem in arr:
        currSum = currSum + elem
        sumArr.append(currSum)
    print sumArr

def sum(arr, begin, end):
    if len(sumArr) == 0:
        primeSumArr()
    return sumArr[end] - sumArr[begin-1] if begin > 0 else sumArr[end]

if __name__ == "__main__":
    arr = [0,1,2,3,4,5,6,7,8,9]
    length = len(arr)
    for i in range(length):
        for j in range(length):
            if j < i: continue
            print "From {0:4d} to {1:4d}: {sum:5d}".format(i, j,sum=sum(arr, i, j))
        print "-" * 20
