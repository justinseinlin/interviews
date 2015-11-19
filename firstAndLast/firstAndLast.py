#! /usr/bin/python

############################################################
# Given a sorted array, find the first and last occurrances
# of a given number in the array.
############################################################

def binarySearch(arr, num, begin, end):
    if begin == end:
        return None

    mid = (end + begin) / 2
    value = arr[mid]
    if value == num:
        return mid
    elif  value < num:
        return binarySearch(arr, num, mid + 1, end)
    else:
        return binarySearch(arr, num, begin, mid)

def getFirstAndLast(arr, num):
    idx = binarySearch(arr, num, 0, len(arr))
    if idx is None:
        return (None, None)

    first = idx
    last = idx
    while first:
        if arr[first - 1] == num:
            first = first - 1
        else:
            break
    while last < len(arr) - 1:
        if arr[last + 1] == num:
            last = last + 1
        else:
            break
    return (first, last)


if __name__ == "__main__":
    arr = [1,1,1,2,2,2,2,2,3,4,4,4,10,12,12]
    DATA = [
        [1, (0,2)],
        [2, (3,7)],
        [3, (8,8)],
        [4, (9,11)],
        [10, (12,12)],
        [12, (13,14)],
        [0, (None, None)],
        [13, (None, None)]
    ]
    print "Array: {0}".format(arr)
    print "-" * 20
    passCount = 0
    for data in DATA:
        expected = data[1]
        actual = getFirstAndLast(arr, data[0])
        print "Num: {0:5}, Expected: {1:15}, Actual: {2:15}, Result: {3}".\
                format(data[0], expected, actual, "PASSED" if expected == actual else "FAILED")
        passCount += 1 if expected == actual else 0
    print "-" * 20
    print "Test Result: {0}".format("PASSED" if passCount == len(DATA) else "FAILED")
