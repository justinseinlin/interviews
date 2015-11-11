#! /usr/bin/python

######################################################################
# Given a prefix notation given a string with space delimited tokens,
# calculate the value of the expression.
######################################################################

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

OPS = {
    '+' : add,
    '-' : subtract,
    '*' : multiply,
    '/' : divide
}
def calc(expr):
    from collections import deque

    def calcHelper(expr):
        if not expr:
            return None

        currToken = expr.popleft()
        if currToken in OPS.keys():
            left = calcHelper(expr)
            right = calcHelper(expr)
            return OPS[currToken](left, right)
        else:
            return currToken

    def parsePrefix(exprStr):
        expr = deque()
        if len(exprStr):
            for curr in exprStr.split(' '):
                expr.append(curr if curr in OPS.keys() else int(curr))
        return expr

    return calcHelper(parsePrefix(expr))

def calcAlt(expr):
    def parsePrefix(exprStr):
        expr = list()
        if len(exprStr):
            for curr in exprStr.split(' '):
                expr.append(curr if curr in OPS.keys() else int(curr))
        return expr

    stack = list()
    parsed = parsePrefix(expr)
    if not parsed: return None
    while parsed:
        curr = parsed.pop()
        if curr in OPS.keys():
            left = stack.pop()
            right = stack.pop()
            stack.append(OPS[curr](left, right))
        else:
            stack.append(curr)
    return stack.pop()

def test():
    DATA = [
        ("", None),
        ("6", 6),
        ("+ 1 2", 3),
        ("+ -1 2", 1),
        ("+ 1 -2", -1),
        ("+ -1 -2", -3),
        ("- 4 2", 2),
        ("- -4 2", -6),
        ("- 4 -2", 6),
        ("- -4 -2", -2),
        ("* 2 3", 6),
        ("* -2 3", -6),
        ("* 2 -3", -6),
        ("* -2 -3", 6),
        ("* 0 3", 0),
        ("/ 6 2", 3),
        ("/ -6 2", -3),
        ("/ 6 -2", -3),
        ("/ -6 -2", 3),
        ("* - 6 2 6", 24),
        ("* - 6 12 6", -36)
    ]
    print "=" * 80
    print "Front to Back method:"
    print "=" * 80
    passCount = 0
    for row in DATA:
        actual = calc(row[0])
        expected = row[1]
        print "Expr: {expr:15}, Actual: {actual:7}, Expected: {expected:7}".\
                format(expr=row[0], actual=actual, expected=expected)
        if actual == expected:
            passCount += 1
    print "=" * 80
    print "Test result: {result}".format(result=("PASSED" if passCount == len(DATA) else "FAILED"))
    print "=" * 80

    print
    print "=" * 80
    print "Back to Front method:"
    print "=" * 80
    passCount = 0
    for row in DATA:
        actual = calcAlt(row[0])
        expected = row[1]
        print "Expr: {expr:15}, Actual: {actual:7}, Expected: {expected:7}".\
                format(expr=row[0], actual=actual, expected=expected)
        if actual == expected:
            passCount += 1
    print "=" * 80
    print "Test result: {result}".format(result=("PASSED" if passCount == len(DATA) else "FAILED"))
    print "=" * 80

if __name__ == "__main__":
    test()


