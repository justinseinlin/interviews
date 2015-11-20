#! /usr/bin/python

###############################################
# Given an unsorted array, remove duplicates
# and report the number of elements left.
###############################################

def countAfterDupRemoval(arr):
    seen = set()
    for elem in arr:
        if elem not in seen:
            seen.add(elem)
    return len(seen)

if __name__ == "__main__":
    DATA = [
        [ [], 0],
        [ [1], 1],
        [ [1,1], 1],
        [ [1,2], 2],
        [ [1,2,2], 2],
        [ [1,2,3], 3],
        [ [1,2,2,3], 3],
        [ [1,2,3,2], 3],
        [ [2,1,2,3], 3],
        [ [1,1,5,3,8,3,7,32,32], 6],
    ]
    passCount = 0
    for data in DATA:
        expected = data[1]
        actual = countAfterDupRemoval(data[0])
        print "Expected: {0:5}, Actual: {1:5}, Result: {2}".\
                format(expected, actual, "PASSED" if expected == actual else "FAILED")
        passCount += 1 if expected == actual else 0
    print "-" * 20
    print "Test Result: {0}".format("PASSED" if passCount == len(DATA) else "FAILED")

