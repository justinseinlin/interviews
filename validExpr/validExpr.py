#! /usr/bin/python

###################################################################
# Validate a bracket-matched expression.
# () is valid
# ({) is not valid
###################################################################
OPENING_BRACKETS = ['(', '{', '[']
MATCHING_OPENING_BRACKETS = {
        ')': '(',
        '}': '{',
        ']': '['
}
def isValidExpr(expr):
    tokens = list()
    for token in expr:
        if token in OPENING_BRACKETS:
            tokens.append(token)
        else:
            if len(tokens) == 0:
                return False

            prev = tokens.pop()
            if MATCHING_OPENING_BRACKETS[token] != prev:
                return False

    return len(tokens) == 0

if __name__ == "__main__":
    DATA = [
        ['', True],
        ['()', True],
        ['{}', True],
        ['[]', True],
        ['(', False],
        ['}', False],
        ['[{()}]', True],
        ['[{(})]', False],
        ['[{()]', False]
    ]
    passCount = 0
    for data in DATA:
        expected = data[1]
        actual = isValidExpr(data[0])
        print "Expr= {0:10}, Expected: {1:5}, Actual: {2:5}, Result: {3}".\
                format(data[0], expected, actual, "PASSED" if expected == actual else "FAILED")
        passCount += 1 if expected == actual else 0

    print "-" * 20
    print "Test Result: {0}".format("PASSED" if passCount == len(DATA) else "FAILED")

