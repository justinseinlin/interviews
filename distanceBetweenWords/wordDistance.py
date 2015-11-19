#! /usr/bin/python
###################################################################
# Given a string and two words which are included in the string,
# find the minimum distance between the two words. If the same word
# appears multiple times, the minimum distance is between the closest
# two such words.
###################################################################

DELIMITER = " "

def distance(string, word1, word2):
    # If isSame is true, the function expects arr1 and arr2
    # to be identical and have at least 2 elements, denoting
    # the positions of the two identical words in the given string.
    def findMinDist(arr1, arr2, isSame=False):
        if isSame:
            min = abs(arr1[0] - arr2[1])
            for i in range(len(arr1)):
                for j in range(len(arr2)):
                    if i == j:
                        continue
                    dist = abs(arr1[i] - arr2[j])
                    if dist < min:
                        min = dist
        else:
            min = abs(arr1[0] - arr2[0])
            for elem1 in arr1:
                for elem2 in arr2:
                    dist = abs(elem1 - elem2)
                    if dist < min:
                        min = dist
        return min

    tokens = string.split(DELIMITER)
    positions = {}
    for i in range(len(tokens)):
        token = tokens[i]
        if token in positions.keys():
            positions[token].append(i)
        else:
            positions[token] = [i]

    pos1 = positions[word1] if word1 in positions.keys() else None
    pos2 = positions[word2] if word2 in positions.keys() else None

    if pos1 is not None and pos2 is not None:
        return findMinDist(pos1, pos2, word1 == word2)
    else:
        return None


if __name__ == "__main__":
    string = "the quick The brown the frog"
    DATA = [
        ["the", "the", 4],
        ["the", "frog", 1],
        ["the", "The", 2],
        ["quick", "the", 1],
        ["quick", "The", 1],
        ["brown", "the", 1],
        ["quick", "brown", 2],
        ["quick", "frog", 4],
        ["brown", "The", 1],
        ["The", "the", 2]
    ]
    print "String = %s" % string
    passCount = 0
    for data in DATA:
        expected = data[2]
        actual = distance(string, data[0], data[1])
        print "Word1: {0:10}, Word2: {1:10}, Expected: {2:5}, Actual: {3:5}, Result: {4}".\
            format(data[0], data[1], expected, actual, "PASSED" if expected == actual else "FAILED")
        passCount += 1 if expected == actual else 0

    print "Test result: {0}".format("PASSED" if passCount == len(DATA) else "FAILED")
